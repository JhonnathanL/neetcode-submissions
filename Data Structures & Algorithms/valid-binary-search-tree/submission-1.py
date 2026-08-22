# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        curr = root

        def isValidNode(curr, min_val, max_val):
            if not curr:
                return True

            if curr.val <= min_val or curr.val >= max_val:
                return False

            return (
                isValidNode(curr.left, min_val, curr.val) and
                isValidNode(curr.right, curr.val, max_val)
            )

        
        return isValidNode(root, float("-inf"), float("inf"))
            

        
        