class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def get_vertices(self):
        return list(self.gdict.keys())

    def get_edges(self):
        return self.find_edges()

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.gdict:
            self.gdict[vertex1].append(vertex2)
        else:
            self.gdict[vertex1] = [vertex2]

# List the edge names
    def find_edges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})

        return edgename


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
