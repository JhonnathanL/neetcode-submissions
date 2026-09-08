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
                return 
            

            dfs(i+1, node.left)
            dfs(i+1, node.right)

            depth = max(depth, i)

            return depth

        if root == None:
            return 0

        dfs(0, root)

        return depth + 1
    

