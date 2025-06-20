"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        originaltocopy = {}
        def dfs(node):
            if node in originaltocopy:
                return originaltocopy[node]
            copy = Node(node.val)
            originaltocopy[node] = copy
            for v in node.neighbors:
                copy.neighbors.append(dfs(v))
            return copy
        if node is not None:
            return dfs(node)
        else:
            return None
        return n
'''
Accepted
22 / 22 testcases passed
Coder174
Coder174
submitted at Jun 20, 2025 19:58

Editorial

Solution
Runtime
39
ms
Beats
81.59%
Analyze Complexity
Memory
18.31
MB
Beats
16.15%
'''      
