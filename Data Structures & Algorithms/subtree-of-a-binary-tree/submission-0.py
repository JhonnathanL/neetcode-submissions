# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(root, subroot):
            if not root and not subroot:
                return True

            if not root or not subroot:
                return False

            if root.val != subroot.val:
                return False
            
            return (isSameTree(root.left, subroot.left) and isSameTree(root.right, subroot.right))

        def findSubtree(root, subroot):
            if not root:
                return False

            if root.val == subroot.val:
                if isSameTree(root, subroot):
                    return True

            return (
                findSubtree(root.left, subroot) or
                findSubtree(root.right, subroot)
            )

        return findSubtree(root, subRoot)
