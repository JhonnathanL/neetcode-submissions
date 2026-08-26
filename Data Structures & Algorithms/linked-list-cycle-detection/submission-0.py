# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        def seeNode(node):
            if not node:
                return False

            if node in visited:
                return True
            
            visited.add(node)

            return seeNode(node.next)

        
        return seeNode(head)