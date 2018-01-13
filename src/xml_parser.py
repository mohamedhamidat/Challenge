import xml.etree.ElementTree as element_tree
from graph import Graph
import os.path

def get_root(file_name): 
    tree = element_tree.parse(file_name)
    root = tree.getroot()
    return root

def get_item_from_root(root, item): 
    return [found_item.text for found_item in root.findall(item)]

def nodes_are_before_edges(root):
    if root[2].tag == 'nodes' and root[3].tag == 'edges':
        return True
    return False

def get_nodes(root):
    nodes = [node for node in root[2].findall('node')]
    _nodes = []
    for node in nodes: 
        node_id = node.find("id").text
        node_name = node.find("name").text
        _nodes.append((node_id, node_name))

    return _nodes

def get_edges(root):
    """
    return list of tuples (id, from, to, cost) of every node in edges
    """
    nodes =  [node for node in root[3].findall('node')]
    edges = []
    for node in nodes:
        id = node.find("id").text
        _from = node.find("from").text
        to = node.find("to").text
        cost = node.find("cost").text if node.find("cost") != None else "0"
        edges.append((id, _from, to, float(cost)))

    return edges

def nodes_have_different_ids(root):
    nodes = get_nodes(root); 
    different_ids = set([node[0] for node in nodes])
    return len(nodes) == len(different_ids)

def edges_have_single_from_and_to_tags(root):
    nodes = [node for node in root[3].findall('node')]
    for node in nodes:
        from_tag = node.findall('from')
        to_tag = node.findall('to')
        if len(from_tag) != 1 or len(to_tag) != 1 :
            return False
    return True

def get_graph_from_root(root):
    
    graph_id = get_item_from_root(root, "id")[0]
    graph_name = get_item_from_root(root, "name")[0]

    graph = Graph(graph_id, graph_name)
    

    nodes = get_nodes(root)
    edges = get_edges(root)

    for node in nodes:
        node_id, node_name = node 
        graph.add_node(node_name)
    

    for node in edges:
        node_id, from_node, to_node, cost = node
        graph.add_edge(from_node, to_node, cost)
        
    return graph