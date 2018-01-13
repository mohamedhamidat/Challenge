import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')

from graph import Graph, get_possible_paths, get_shortest_path
import unittest

class Test_Graph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph("g1", "the Graph")
        for node in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
          self.graph.add_node(node)

        self.graph.add_edge('A', 'B', 10)
        self.graph.add_edge('A', 'C', 1)
        self.graph.add_edge('B', 'D', 1.9)
        self.graph.add_edge('C', 'D', 2)
        self.graph.add_edge('B', 'E', 44)
        self.graph.add_edge('D', 'E', 7)
        self.graph.add_edge('E', 'F', 5)
        self.graph.add_edge('F', 'G', 2)
    
    def test_get_possible_paths(self):
        start = "A"
        end = "E"
        
        paths = get_possible_paths(self.graph, start, end)

        self.assertEqual(len(paths), 3)
        self.assertEqual(['A', 'B', 'D', 'E'] in paths, True)

    def test_get_shortest_path(self):  
        start = "A"
        end = "E"

        path = get_shortest_path(self.graph, start, end)

        self.assertEqual(['A', 'C', 'D', 'E'], path)
    
    def test_get_shortest_path_if_not_exisit(self):   
        start = "A"
        end = "S"

        path = get_shortest_path(self.graph, start, end)

        self.assertEqual([], path)


def main():
    unittest.main()

if __name__ == "__main__":
    main()