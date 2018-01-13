from collections import defaultdict, deque

class Graph(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name 
        self.nodes = set()
        self.edges = defaultdict(list)
        self.costs = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, cost):
        self.edges[from_node].append(to_node)
        self.costs[(from_node, to_node)] = cost

def dijkstra(graph, initial):
    """
    Dijkstra's algorithm solves the shortest path from one node 
    to all the other nodes in a weighted graph with no negative weight edges. 
    """


    visited_nodes = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        closet_node = None
        for node in nodes:
            if node in visited_nodes:
                if closet_node is None:
                    closet_node = node
                elif visited_nodes[node] < visited_nodes[closet_node]:
                    closet_node = node
        if closet_node is None:
            break

        nodes.remove(closet_node)
        current_weight = visited_nodes[closet_node]

        for edge in graph.edges[closet_node]:
            try:
                weight = current_weight + graph.costs[(closet_node, edge)]
            except:
                continue
            if edge not in visited_nodes or weight < visited_nodes[edge]:
                visited_nodes[edge] = weight
                path[edge] = closet_node

    return visited_nodes, path

def get_shortest_path(graph, origin, destination):
    """
    return a list shortest path if exisits 
    """
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    if destination in paths: 
        _destination = paths[destination]
        
        while _destination != origin:
            full_path.appendleft(_destination)
            _destination = paths[_destination]

        full_path.appendleft(origin)
        full_path.append(destination)

    return list(full_path)

def get_all_paths_helper(graph, _from, to, visited, path, paths):
    
    # Mark the current node as visited and store in path
    visited.append(_from)
    path = path + [_from]

    # If current node is same as destination, then print
    # current path[]
    if _from == to:
        path = path + [to]
        paths.append(path)
    else:
        # If current vertex is not destination
        #Recur for all the nodes adjacent to this node
        for destination in graph.edges[_from]:
            if destination not in visited:
                get_all_paths_helper(graph, destination, to, visited, path, paths)
                    
    # Remove current node from path[] and mark it as unvisited
    path.pop()
    visited.remove(_from)

def get_possible_paths(graph, _from, _to):
    """
    return all possible paths using Breadth-first search (BFS)
    graph search algorithm that begins in a specified node and explores the neighboring nodes 

    """
    # Mark all the nodes as not visited
    visited = []
    cost = {}

    # Create an array to store paths
    path = []
    paths = []

    # Call the recursive helper function to get all paths
    get_all_paths_helper(graph, _from, _to, visited, path, paths)

    return paths