import random

class Maze:
    def __init__(self, num_vertices, num_edges):
        self.graph = {i: [] for i in range(num_vertices)}
        for i in range(num_vertices):
            edges = random.sample([j for j in range(num_vertices) if j != i], min(num_edges, num_vertices-1))
            self.graph[i] = edges

    def get_possible_directions(self, vertex):
        return self.graph.get(vertex, [])
