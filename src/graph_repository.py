"""
repository which mediates between the domain and data mapping layers acting like in memory collection of domain objects
In this I'm simulatig have an ORM to insert values into graph, node, edge tables 
Also i'm getting data from xml instead of db when get method get called 
"""
from graph import Graph
from xml_parser import get_nodes, get_edges, get_item_from_root, get_graph_from_root
from xml_parser import get_root

def add(graph_xml):
    """
    add graph to db
    """ 
    graph_id = get_item_from_root(graph_xml, "id")
    graph_name = get_item_from_root(graph_xml, "name")

    #ORM.Add_Graph_To_Graph_TABLE(graph_id, graph_name)
    

    nodes = get_nodes(graph_xml)
    edges = get_edges(graph_xml)

    for node in nodes:
        node_id, node_name = node 
        #ORM.Add_Node_To_Node_TABLE(node_name, node_id, graph_id)
    

    for node in edges:
        node_id, from_node, to_node, cost = node
        #ORM.Add_Edge_To_Edge_TABLE(node_id, from_node, to_node, cost, graph_id)

def remove(id):
    pass

def get(id):
    root = get_root("graph.xml")
    graph = get_graph_from_root(root)

    return graph
