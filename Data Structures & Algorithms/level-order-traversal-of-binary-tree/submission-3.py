# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        levels = {}

        def dfs(i, node):
            nonlocal levels

            if not node:
                return
            
            i += 1

            if i not in levels:
                levels[i] = []
            
            levels[i].append(node.val)

            dfs(i, node.left)
            dfs(i, node.right)


        dfs(0, root)    

        return list(levels.values())
