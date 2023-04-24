class Graph:
    def __init__(self, graph_dict = None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def get_vertices(self):
        return list(self.graph_dict.keys())

    def get_edges(self):
        return self.find_edges()

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]

# List the edge names
    def find_edges(self):
        edges = []
        for start in self.graph_dict:
            for end in self.graph_dict[start]:
                if (end, start) not in edges:
                    edges.append((start, end))

        return edges


graph_elements = {
   "a": ["b", "c"],
   "b": ["a", "d"],
   "c": ["a", "d"],
   "d": ["e"],
   "e": ["d"]
}

g = Graph(graph_elements)
g.add_edge({"a", "e"})
print(g.get_vertices())
print(g.get_edges())
