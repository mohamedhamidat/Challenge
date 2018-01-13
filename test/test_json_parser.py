import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')


import unittest
from json_parser import get_queries, get_all_queries
import json

class Test_json_parser(unittest.TestCase): 

    def test_get_queries(self):
        input = """
        {
            "queries": [
            {
                "paths": 
                {
                "start": "a",
                "end": "e"
                }
            },
            {
                "cheapest": {
                "start": "a",
                "end": "e"
                }
                }
            ]
        }
        """
        data = json.loads(input)
        paths = get_queries(data, "paths")
        cheapests = get_queries(data, "cheapest")

        self.assertEqual(len(paths), 1)
        self.assertEqual(len(cheapests), 1)


    def test_get_queries(self):
        input = """
        {
            "queries": [
            {
                "paths": 
                {
                "start": "a",
                "end": "e"
                }
            },
            {
                "cheapest": {
                "start": "a",
                "end": "e"
                }
                }
            ]
        }
        """
        data = json.loads(input)
        queries = get_all_queries(data)

        self.assertEqual(len(queries), 2)

def main():
    unittest.main()

if __name__ == "__main__":
    main()