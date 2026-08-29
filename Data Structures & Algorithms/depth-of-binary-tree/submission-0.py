# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        depth = 0

        def dfs(i, node):
            nonlocal depth

            if not node:
                return 0
            
            left = dfs(i+1, node.left)
            right = dfs(i+1, node.right)

            depth = max(depth, i)


        dfs(1, root)

        return depth 