#The problem is to print the topological sorting of a graph using bfs
#The key is to use indegree
from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.graph = defaultdict(list)
        for i in range(n):
            self.graph[i] = []
        self.visited = [0]*n
    def addEdge(self,u,v):
        # print(f'{u},{v}\n')
        self.graph[u].append(v)
        # print(self.graph[u])
    def bfs(self):
        indegree = {}
        toposort = []
        for i in self.graph:
            indegree[i] = 0
        queue = []
        for i in self.graph:
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            s = queue.pop(0)
            toposort.insert(0,s)
            for v in self.graph[s]:
                indegree[v] = indegree[v] -1
                if indegree[v] == 0:
                    queue.append(indegree[v])
            
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
g.bfs()
