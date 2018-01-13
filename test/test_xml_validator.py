import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')

import unittest
import xml.etree.ElementTree as element_tree
from xml_validator import is_valid_graph, file_exists


class Test_xml_validator(unittest.TestCase):
    
    def test_file_exisits(self):
        result = file_exists("nofile.xml")
        self.assertEqual(result, False)
    
    def test_is_valid_xml(self):
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

        result = is_valid_graph(root)

        self.assertEqual(result, True)

def main():
    unittest.main()

if __name__ == "__main__":
    main()