"""
Just a model to simulate json request
"""
import json 
def get_json_queries():
    input = """
            {
            "queries": [
                {
                "paths": {
                    "start": "A",
                    "end": "D"
                }
                },
                {
                "paths": {
                    "start": "A",
                    "end": "B"
                }
                },
                {
                "cheapest": {
                    "start": "A",
                    "end": "C"
                }
                },
                {
                "cheapest": {
                    "start": "A",
                    "end": "N"
                }
                }
            ]
            }
    """ 
    data = json.loads(input)["queries"]
    return data 
