"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        copies = {}

        def dfs(curr):
            if curr in copies:
                return copies[curr]

            copy = Node(curr.val)
            copies[curr] = copy

            for neighbors in curr.neighbors:
                copy.neighbors.append(dfs(neighbors))
            
            return copy
        
        return dfs(node)

            
        