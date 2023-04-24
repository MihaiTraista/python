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
        for vertex in self.graph_dict:
            for next_vertex in self.graph_dict[vertex]:
                if (next_vertex, vertex) not in edges:
                    edges.append((vertex, next_vertex))

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
g.add_edge({"a", "c"})
print(g.get_vertices())
print(g.get_edges())
