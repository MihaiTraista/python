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


class Graph:
    def __init__(self, graph_edges):
        self.nodes = set()
        for edge in graph_edges:
            self.nodes.update([edge[0], edge[1]])

        self.adjacency_list = {node: set() for node in self.nodes}
        for edge in graph_edges:
            self.adjacency_list[edge[0]].add((edge[1], edge[2]))



g = Graph(edges)

