class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def bfs(graph):
            indegree = {}
            for i in graph:
                indegree[i] = 0
            for i in graph:
                for v in graph[i]:
                    indegree[v] += 1
            queue = []
            for i in indegree:
                if indegree[i] == 0:
                    queue.append(i)
            topo = []
            while queue:
                s = queue.pop(0)
                topo.insert(0,s)
                for v in graph[s]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        queue.append(v)
            if len(topo) < numCourses:
                return False
            else:
                return True
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for element in prerequisites:
            graph[element[0]].append(element[1])
        return bfs(graph)
'''
Accepted
54 / 54 testcases passed
Coder174
Coder174
submitted at Jun 21, 2025 11:38

Editorial

Solution
Runtime
7
ms
Beats
46.76%
Analyze Complexity
Memory
18.98
MB
Beats
82.87%

'''
