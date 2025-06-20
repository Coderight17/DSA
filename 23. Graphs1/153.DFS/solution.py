from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.graph = defaultdict(list)
        self.visited = [False]*n
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def dfs_visit(self, u):
        self.visited[u] = True
        print(u, end = ' ')
        for v in self.graph[u]:
            if not self.visited[v]:
                self.dfs_visit(v)
    def dfs(self):
        for i in self.graph:
            if not  self.visited[i]:
                self.dfs_visit(i)
                print('\n', end = '')
n= int(input('Enter no of vertices'))
g = Graph(n)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
# g.dfs()
g.dfs_visit(2)
