from __future__ import annotations
import time 
from functools import reduce
from functools import total_ordering # used for implemeting all ordering things
import heapq
import math


class Queue: 

    def __init__(self): 
        pq = [] # heapq
    
    def add_item(self, item: Vertex): 
        pass 



@total_ordering 
class Vertex:

    def __init__(self, i, j, weight): 
        self.i: int = i
        self.j: int = j 
        self.weight: int = weight
        self.edges: list[Vertex] = []
        self.distance: float = math.inf
        self.prev: Vertex | None = None 
    
    def add_edge(self, other: Vertex) -> None: 
        self.edges.append(other)

    def __lt__(self, other: Vertex) -> bool: 
        return self.distance < other.distance
    
    def __eq__(self, other: Vertex) -> bool: 
        return self.distance == other.distance 
    
    def __str__(self) -> str: 
        return '{weight}: {edges}'.format(weight = str(self.weight), edges=[edge.weight for edge in self.edges])

class Graph: 

    def __init__(self, vertex_weights): 
        self.size: tuple[int, int] = (len(vertex_weights), len(vertex_weights[0]))
        self.vertices: list[list[Vertex]] = [[Vertex(i, j, vertex_weights[i][j]) for j in range(self.size[1])] 
                                                    for i in range(self.size[0])]
        self.vertices_flat: list[Vertex] = reduce(lambda x, y: x+y, self.vertices)
        self.initial = self.vertices[0][0]
        self.set_edges()

    def get_goal(self): 
        return self.vertices[self.size[0] - 1][self.size[1] - 1]

    def set_edges(self):
        for i in range(len(self.vertices)): 
            for j in range(len(self.vertices[0])): 
                if i > 0: self.vertices[i][j].add_edge(self.vertices[i - 1][j])
                if j > 0: self.vertices[i][j].add_edge(self.vertices[i][j - 1])
                if i < self.size[0] - 1: self.vertices[i][j].add_edge(self.vertices[i + 1][j])
                if j < self.size[1] - 1: self.vertices[i][j].add_edge(self.vertices[i][j + 1])
    
    def __str__(self): 
        return reduce(lambda x, y: str(x) + "\n" + str(y), self.vertices_flat)
    
def dijkstra(graph: Graph): 
    graph.initial.distance = 0 
    Q = PriorityQueue() 
    for vertex in graph.vertices_flat: 
        Q.put(vertex)
    
    while not Q.empty(): 
        vertex: Vertex = Q.get()   # extract vertex with minimal distance 
        print(vertex.distance)
        for neighbour in vertex.edges: 
            new_dist = vertex.distance + neighbour.weight
            if (new_dist < neighbour.distance): 
                neighbour.distance = new_dist
                neighbour.prev = vertex 

def get_input(): 
    with open('./2023/day17/testinput.txt') as f: 
        lines = [[int(char) for char in line.strip()] for line in f.readlines()]
        return Graph(vertex_weights=lines)
    
def part1(graph: Graph):
    dijkstra(graph)
    print(graph.get_goal().distance)
    return 0

def part2(input): 
    return 0

def main(): 
    input = get_input()
    time_start = time.time() 
    answer = part1(input)
    time_end = time.time()
    print('answer part 1:', answer)
    print('running time: ', time_end - time_start, '\n')
    
    time_start = time.time() 
    answer = part2(input)
    time_end = time.time()
    print('\nanswer part 2:', answer)
    print('running time: ', time_end - time_start, '\n')

if __name__ == "__main__": 
    main()
