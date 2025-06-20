class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs_visit(graph,visited,u):
            visited[u] = 1
            for v in graph[u]:
                if visited[v] == 0:
                    # visited[v] = 1
                    fg = dfs_visit(graph,visited,v)
                    if not fg:
                        return False
                else:
                    if visited[v] == 1:
                        return False
            visited[u] = 2
            return True
        def dfs(graph,visited):
            for i in graph:
                if visited[i] == 0:
                    fg = dfs_visit(graph,visited,i)
                    if not fg:
                        return False
            return True
        graph = {}
        for i in range(numCourses):
            graph[i] = set()
        for element in prerequisites:
            graph[element[0]].add(element[1])
        visited = [0]*numCourses
        return dfs(graph,visited)
'''
Accepted
54 / 54 testcases passed
Coder174
Coder174
submitted at Jun 20, 2025 21:42

Editorial

Solution
Runtime
3
ms
Beats
88.00%
Analyze Complexity
Memory
19.10
MB
Beats
61.51%

'''
