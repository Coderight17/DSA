#BREADTH FIRST SEARCH(BFS) in Python
from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.graph = defaultdict(list)
        self.visited = [False]*n
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def bfs(self, u):
        queue = [u]
        print(u, end = ' ')
        self.visited[u] = True
        while queue:
            s = queue.pop(0)
            for v in self.graph[s]:
                if not self.visited[v]:
                    self.visited[v] = True
                    queue.append(v)
                    print(v, end = ' ')
        print('\n', end = '')
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.bfs(2)
    
