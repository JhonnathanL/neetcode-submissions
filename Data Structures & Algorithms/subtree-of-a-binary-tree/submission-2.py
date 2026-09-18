# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check_tree(node, subroot):
            if not node and not subroot:
                return True
            
            if not node or not subroot:
                return False
            
            if node.val != subroot.val:
                return False
            
            return (check_tree(node.left,subroot.left) and check_tree(node.right, subroot.right))
        

        def dfs(node, subroot):
            if not node:
                return False
            
            if node.val == subroot.val:
                if check_tree(node, subroot):
                    return True

            return (dfs(node.right, subroot) or dfs(node.left, subroot))
        

        return dfs(root, subRoot)


