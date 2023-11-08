from collections import deque

class Graph:
    def _init_(self, vertices):
        self.vertices = vertices
        self.adj_list = {i: [] for i in range(vertices)}

    def add_edge(self, start, end):
        self.adj_list[start].append(end)

    def bfs(self, start_node):
        visited = [False] * self.vertices
        traversal_order = []
        queue = deque([start_node])
        visited[start_node] = True

        while queue:
            node = queue.popleft()
            traversal_order.append(node)
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

        return traversal_order

    def dfs(self, start_node):
        visited = [False] * self.vertices
        traversal_order = []

        def dfs_recursive(node):
            traversal_order.append(node)
            visited[node] = True
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    dfs_recursive(neighbor)

        dfs_recursive(start_node)
        return traversal_order

def main():
    num_nodes = int(input("Enter the number of nodes: "))
    num_edges = int(input("Enter the number of edges: "))
    
    graph = Graph(num_nodes)

    for _ in range(num_edges):
        start, end = map(int, input("Enter an edge (start end): ").split())
        graph.add_edge(start, end)

    while True:
        print("\nMenu:")
        print("Case B/b: BFS Traversal")
        print("Case D/d: DFS Traversal")
        print("Case T/t: Both BFS and DFS traversal")
        print("Case X/x: Exit")

        choice = input("Enter your choice: ").lower()

        if choice == 'b':
            start_node_bfs = int(input("Enter the starting node for BFS: "))
            bfs_order = graph.bfs(start_node_bfs)
            print("BFS Traversal Order:", bfs_order)
        elif choice == 'd':
            start_node_dfs = int(input("Enter the starting node for DFS: "))
            dfs_order = graph.dfs(start_node_dfs)
            print("DFS Traversal Order:", dfs_order)
        elif choice == 't':
            start_node_both = int(input("Enter the starting node for both BFS and DFS: "))
            bfs_order = graph.bfs(start_node_both)
            dfs_order = graph.dfs(start_node_both)
            print("BFS Traversal Order:", bfs_order)
            print("DFS Traversal Order:", dfs_order)
        elif choice == 'x':
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
