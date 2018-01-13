"""
This module for parsing json format
"""
import json

def get_queries(data_json, query):
    """
    return a list of query (path or cheapest)
    """
    return [path_cheapest[query] for path_cheapest in data_json if query in path_cheapest]

def get_all_queries(data_json): 
    return data_json["queries"]