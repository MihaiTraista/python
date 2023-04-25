#   https://github.com/dmahugh/dijkstra-algorithm/blob/master/dijkstra_algorithm.py

edges = [
    ["A", "B", 5],
    ["A", "C", 3],
    ["A", "D", 6],
    ["B", "C", 6],
    ["B", "E", 4],
    ["C", "E", 6],
    ["C", "D", 7],
    ["D", "F", 2],
    ["D", "E", 2],
    ["E", "G", 3],
    ["E", "F", 4],
    ["F", "G", 5]
]

INFINITY = float("inf")

class Graph:
    def __init__(self, graph_edges):
        self.nodes = set()
        for edge in graph_edges:
            self.nodes.update([edge[0], edge[1]])

        # unordered set of (neighbor, distance) tuples
        self.graph_dict = {node: set() for node in self.nodes}
        for edge in graph_edges:
            self.graph_dict[edge[0]].add((edge[1], edge[2]))

    def shortest_path(self, start_node, end_node):
        # returns (path, distance)

        unvisited_nodes = self.nodes.copy()  # All nodes are initially unvisited.

        # Create a dictionary of each node's distance from start_node. We will
        # update each node's distance whenever we find a shorter path.
        distance_from_start = {
            node: (0 if node == start_node else INFINITY) for node in self.nodes
        }

        # Initialize previous_node, the dictionary that maps each node to the
        # node it was visited from when the shortest path to it was found.
        previous_node = {node: None for node in self.nodes}


g = Graph(edges)

print(g.graph_dict["C"])
