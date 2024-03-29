#   https://github.com/dmahugh/dijkstra-algorithm/blob/master/dijkstra_algorithm.py

from collections import deque

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

        while unvisited_nodes:
            # Set current_node to the unvisited node with shortest distance
            # calculated so far.
            current_node = min(
                unvisited_nodes, key=lambda node: distance_from_start[node]
            )
            unvisited_nodes.remove(current_node)

            # If current_node's distance is INFINITY, the remaining unvisited
            # nodes are not connected to start_node, so we're done.
            if distance_from_start[current_node] == INFINITY:
                break

            # For each neighbor of current_node, check whether the total distance
            # to the neighbor via current_node is shorter than the distance we
            # currently have for that node. If it is, update the neighbor's values
            # for distance_from_start and previous_node.
            for neighbor, distance in self.graph_dict[current_node]:
                new_path = distance_from_start[current_node] + distance
                if new_path < distance_from_start[neighbor]:
                    distance_from_start[neighbor] = new_path
                    previous_node[neighbor] = current_node

            if current_node == end_node:
                break  # we've visited the destination node, so we're done

        # To build the path to be returned, we iterate through the nodes from
        # end_node back to start_node. Note the use of a deque, which can
        # append left with O(1) performance.
        path = deque()
        current_node = end_node
        while previous_node[current_node] is not None:
            path.appendleft(current_node)
            current_node = previous_node[current_node]
        path.appendleft(start_node)

        return path, distance_from_start[end_node]


g = Graph(edges)

print(g.graph_dict["C"])
print(g.shortest_path("B", "D"))
