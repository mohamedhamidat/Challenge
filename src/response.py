
import json
from collections import OrderedDict
from json_parser import get_queries
import graph_repository 
from graph import get_possible_paths, get_shortest_path 


def get_response(query):
    """
    return one json answer with all queries with this fromt 

    {
        "answers": [
            {
            "cheapest": {
                "from": "a",
                "to": "b",
                "path": ["a", "b"]
            },
            ....
        ]
    }

    """


    #get the graph object from db (in this case just from xml)
    graph = graph_repository.get("graph_id")

    query_paths = get_queries(query, "paths")
    query_cheapest = get_queries(query, "cheapest")

    paths = []
    for path in query_paths: 
        start = path["start"]
        end = path["end"]
        possible_paths = get_possible_paths(graph, start, end)
        path = OrderedDict()
        path["from"] = start
        path["to"] = end
        path["paths"] = possible_paths
        paths.append({"paths" : path})

    cheapest = []
    for path in query_cheapest: 
        start = path["start"]
        end = path["end"]
        shortest_path = get_shortest_path(graph, start, end)
        path = OrderedDict()
        path["from"] = start
        path["to"] = end
        path["path"] = shortest_path if shortest_path else False
        cheapest.append({"cheapest" : path})
    

    answers = []
    answers.extend(paths)
    answers.extend(cheapest)
    return json.dumps({"answers" : answers})
    

