#The problem is to print the topological sort using dfs
from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.graph = defaultdict(list)
        for i in range(n):
            self.graph[i] = []
        self.visited = [0]*n
    def addEdge(self,u,v):
        print(f'{u},{v}\n')
        self.graph[u].append(v)
        print(self.graph[u])
    def dfs_visit(self, u,toposort):
        self.visited[u] = 1
        for v in self.graph[u]:
            if not self.visited[v]:
                self.dfs_visit(v,toposort)
        self.visited[u] = 2
        toposort.insert(0,u)
    def dfs(self):
        toposort = []
        for i in self.graph:
            if self.visited[i] == 0:
                self.dfs_visit(i,toposort)
        for i in toposort:
            print(i, end = ' ')
        print('\n', end = '')
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
print(g.graph)
g.dfs()
