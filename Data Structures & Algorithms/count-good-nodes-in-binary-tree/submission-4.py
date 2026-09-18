# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0

        good_nodes = 0
        
        def dfs(node, max_value = float("-inf")):
            nonlocal good_nodes

            if not node:
                return 
            
            if node.val >= max_value:
                good_nodes+=1
                max_value = node.val
            
            dfs(node.right, max_value)
            dfs(node.left, max_value)

        
        dfs(root)

        return good_nodes

