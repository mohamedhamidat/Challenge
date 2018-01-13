import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')


import unittest
from xml_parser import (get_item_from_root, 
                        nodes_are_before_edges, 
                        get_nodes, 
                        nodes_have_different_ids, 
                        get_edges,
                        edges_have_single_from_and_to_tags, 
                        get_graph_from_root)

import xml.etree.ElementTree as element_tree


class Test_xml_parser(unittest.TestCase):
    
    def test_get_item_from_root_when_id_names_exist(self):
        xml_string = """
        <graph>
            <id>g0</id>
            <name>The Graph Name</name>
        </graph>       
        """
        tree = element_tree.ElementTree(element_tree.fromstring(xml_string))
        root = tree.getroot()

        id = get_item_from_root(root, 'id')
        name = get_item_from_root(root, 'name')

        self.assertEqual(id, ['g0'])
        self.assertEqual(name , ['The Graph Name'])
    
    def test_get_item_from_root_when_id_names_doesnt_exist(self):
        xml_string = """
        <graph>
        </graph>       
        """
        tree = element_tree.ElementTree(element_tree.fromstring(xml_string))
        root = tree.getroot()

        id = get_item_from_root(root, 'id')
        name = get_item_from_root(root, 'name')

        self.assertEqual(id, [])
        self.assertEqual(name , [])
    
    def test_nodes_are_before_edges_should_return_True(self):    
        xml_string = """
        <graph>
            <id>g0</id>
            <name>The Graph Name</name>
            <nodes>
            </nodes>
            <edges>
            </edges>
        </graph>   
        """
        tree = element_tree.ElementTree(element_tree.fromstring(xml_string))
        root = tree.getroot()

        result = nodes_are_before_edges(root)

        self.assertEqual(result, True)

    def test_nodes_are_before_edges_should_return_False(self):    
        xml_string = """
        <graph>
            <id>g0</id>
            <name>The Graph Name</name>
            <edges>
            </edges>
            <nodes>
            </nodes>
        </graph>   
        """
        tree = element_tree.ElementTree(element_tree.fromstring(xml_string))
        root = tree.getroot()

        result = nodes_are_before_edges(root)

        self.assertEqual(result, False)
    
    def test_get_nodes_if_they_exisit(self):
        xml_string = """
        <graph>
            <id>g0</id>
            <name>The Graph Name</name>
            <nodes>
                <node>
                    <id>a</id>
                    <name>A</name>
                </node>
                <node>
                    <id>e</id>
                    <name>E</name>
                </node>
            </nodes>
            <edges>
            </edges>
        </graph>   
        """
        tree = element_tree.ElementTree(element_tree.fromstring(xml_string))
        root = tree.getroot()

        nodes = get_nodes(root)

        self.assertEqual(2, len(nodes))

    def test_get_nodes_if_they_dont_exisit(self):
        xml_string = """
        <graph>
            <id>g0</id>
            <name>The Graph Name</name>
            <nodes>
            </nodes>
            <edges>
            </edges>
        </graph>   
        """
        tree = element_tree.ElementTree(element_tree.fromstring(xml_string))
        root = tree.getroot()

        nodes = get_nodes(root)

        self.assertEqual(0, len(nodes))

    def test_nodes_have_different_ids_when_True(self):
        xml_string = """
        <graph>
            <id>g0</id>
            <name>The Graph Name</name>
            <nodes>
                <node>
                    <id>a</id>
                    <name>A</name>
                </node>
                <node>
                    <id>e</id>
                    <name>E</name>
                </node>
            </nodes>
            <edges>
            </edges>
        </graph>   
        """
        tree = element_tree.ElementTree(element_tree.fromstring(xml_string))
        root = tree.getroot()

        result = nodes_have_different_ids(root)

        self.assertEqual(result, True)

    def test_nodes_have_different_ids_when_False(self):
        xml_string = """
        <graph>
            <id>g0</id>
            <name>The Graph Name</name>
            <nodes>
                <node>
                    <id>a</id>
                    <name>A</name>
                </node>
                <node>
                    <id>a</id>
                    <name>E</name>
                </node>
            </nodes>
            <edges>
            </edges>
        </graph>   
        """
        tree = element_tree.ElementTree(element_tree.fromstring(xml_string))
        root = tree.getroot()

        result = nodes_have_different_ids(root)

        self.assertEqual(result, False)

    def test_get_edges(self):
        xml_string = """
        <graph>
            <id>g0</id>
            <name>The Graph Name</name>
            <nodes>
            </nodes>
            <edges>
                <node>
                    <id>e1</id>
                    <from>a</from>
                    <to>e</to>
                    <cost>0.42</cost>                    
                </node>
                <node>
                    <id>e5</id>
                    <from>a</from>
                    <to>a</to>
                    <cost>0.42</cost>
                </node>
            </edges>
        </graph>   
        """
        tree = element_tree.ElementTree(element_tree.fromstring(xml_string))
        root = tree.getroot()

        nodes = get_edges(root)

        self.assertEqual(len(nodes), 2)

    def test_get_edges_should_return_cost_zero_when_cost_tag_is_absent(self):
        xml_string = """
        <graph>
            <id>g0</id>
            <name>The Graph Name</name>
            <nodes>
            </nodes>
            <edges>
                <node>
                    <id>e1</id>
                    <from>a</from>
                    <to>e</to>
                </node>
                <node>
                    <id>e5</id>
                    <from>a</from>
                    <to>a</to>
                    <cost>0.42</cost>
                </node>
            </edges>
        </graph>   
        """
        tree = element_tree.ElementTree(element_tree.fromstring(xml_string))
        root = tree.getroot()

        nodes = get_edges(root)
        cost_node1 = nodes[0][3]
        cost_node2 = nodes[1][3]
        
        self.assertEqual(cost_node1, 0.0)
        self.assertEqual(cost_node2, 0.42)

    def test_edges_have_single_from_and_to_tags_when_true(self):
        xml_string = """
        <graph>
            <id>g0</id>
            <name>The Graph Name</name>
            <nodes>
            </nodes>
            <edges>
                <node>
                    <id>e1</id>
                    <from>a</from>
                    <to>e</to>
                    <cost>42</cost>
                </node>
                <node>
                    <id>e5</id>
                    <from>a</from>
                    <to>a</to>
                    <cost>0.42</cost>
                </node>
            </edges>
        </graph>   
        """
        tree = element_tree.ElementTree(element_tree.fromstring(xml_string))
        root = tree.getroot()

        result = edges_have_single_from_and_to_tags(root)

        self.assertEqual(result, True)

    def test_edges_have_single_from_and_to_tags_when_false(self):
        xml_string = """
        <graph>
            <id>g0</id>
            <name>The Graph Name</name>
            <nodes>
            </nodes>
            <edges>
                <node>
                    <id>e1</id>
                    <from>a</from>
                    <from>a</from>
                    <to>e</to>
                    <cost>42</cost>
                </node>
                <node>
                    <id>e5</id>
                    <from>a</from>
                    <to>a</to>
                    <cost>0.42</cost>
                </node>
            </edges>
        </graph>   
        """
        tree = element_tree.ElementTree(element_tree.fromstring(xml_string))
        root = tree.getroot()

        result = edges_have_single_from_and_to_tags(root)

        self.assertEqual(result, False)

    def test_get_graph_from_root(self):
        xml_string = """
        <graph>
            <id>g0</id>
            <name>The Graph</name>
            <nodes>
            </nodes>
            <edges>
                <node>
                    <id>e1</id>
                    <from>a</from>
                    <to>e</to>
                    <cost>42</cost>
                </node>
                <node>
                    <id>e5</id>
                    <from>a</from>
                    <to>a</to>
                    <cost>0.42</cost>
                </node>
            </edges>
        </graph>   
        """
        tree = element_tree.ElementTree(element_tree.fromstring(xml_string))
        root = tree.getroot()

        graph = get_graph_from_root(root)

        self.assertEqual(graph.id, "g0")
        self.assertEqual(graph.name, "The Graph")


def main():
    unittest.main()

if __name__ == "__main__":
    main()