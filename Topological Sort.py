from collections import defaultdict
from queue import Queue

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def topological_sort(self):
        in_degree = [0] * self.V
        
        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1
        
        queue = Queue()
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.put(i)
                
        topo_order = []
        while not queue.empty():
            u = queue.get()
            topo_order.append(u)
            
            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.put(v)
                    
        return topo_order

graph = Graph(7)
graph.add_edge(6, 3)
graph.add_edge(6, 1)
graph.add_edge(5, 3)
graph.add_edge(5, 2)
graph.add_edge(3, 4)
graph.add_edge(4, 2)
graph.add_edge(2, 1)

result = graph.topological_sort()
print("Topological Sort:", result)
