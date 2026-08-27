# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = {}

        def Tree(i, node):
            
            if not node:
                return 
            
            if i not in res:
                res[i] = []

            res[i].append(node.val)


            Tree(i + 1, node.left)
            Tree(i + 1, node.right)

        Tree(0, root)

        return list(res.values())