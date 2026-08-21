# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def compareTree(node, node2):
            if not node and not node2:
                return True
            
            if not node or not node2:
                return False

            if node.val != node2.val:
                return False
            
            return (compareTree(node.left, node2.left) and
            compareTree(node.right, node2.right))

        return compareTree(p, q)
