class Graph:
    def __init__(self):
        self.graph = {}
 
    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
 
    def dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
 
        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)
 
    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)
 
    def bfs(self, start):
        visited = set()
        queue = [start]
 
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                for neighbor in self.graph.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
 
 

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
# g.add_edge(3, 3)
 
print("DFS:")
g.dfs(2)
print("\nBFS:")
g.bfs(2)
