from os import path
from xml_parser import (get_item_from_root, 
                        nodes_are_before_edges, 
                        get_nodes, 
                        nodes_have_different_ids, 
                        get_edges,
                        edges_have_single_from_and_to_tags)

def file_exists(file_name): 
    """
    Check if the file exists
    return True if it exists 
    else return False
    """
    return path.exists(file_name)


def is_valid_graph(root): 
    """
    return True if these applied : 
        • There must be an <id> and <name> for the <graph>.
        • Assume the <nodes> group will always come before the <edges> group.
        • There must be at least one <node> in the <nodes> group.
        • All nodes must have different <id> tags.
        • For every <edge>, there must be a single <from> tag and a single <to> tag, 
            corresponding to nodes that must have been defined before.
    """

    if (get_item_from_root(root, 'id') 
        and get_item_from_root(root, 'name')
        and nodes_are_before_edges(root) 
        and get_nodes(root) 
        and nodes_have_different_ids(root) 
        and edges_have_single_from_and_to_tags(root)):
        
        return True
    
    return False 