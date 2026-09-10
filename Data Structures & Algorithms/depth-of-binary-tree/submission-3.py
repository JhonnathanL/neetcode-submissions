# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(i, node):
            if not node:
                return i

            return max(dfs(i + 1, node.left), dfs(i + 1, node.right))

        return dfs(0, root)