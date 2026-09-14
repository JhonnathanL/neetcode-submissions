# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def is_same(node, subnode):
            if not node and not subnode:
                return True

            if not node or not subnode:
                return False

            if node.val != subnode.val:
                return False
            
            return (is_same(node.left, subnode.left) and is_same(node.right, subnode.right))

        def dfs(node, subnode):
            if not node:
                return False

            if is_same(node, subnode):
                return True
            
            return (dfs(node.left, subnode) or dfs(node.right, subnode))
            
        return dfs(root, subRoot)

