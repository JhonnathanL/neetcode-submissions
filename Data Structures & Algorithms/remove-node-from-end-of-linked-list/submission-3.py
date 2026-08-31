# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        values = []
        
        def removeNode(i, node):
            nonlocal values

            if not node:
                return
            
            values.append(node)
            removeNode(i + 1, node.next)

        def removeNodeValue(i, node, value, prev = None):
            if not node:
                return
            
            if node == value:
                if prev:
                    prev.next = node.next
                    return

            prev = node
            removeNodeValue(i + 1, node.next, value, prev)


        removeNode(0, head)
        if values[-n] == head:
            return head.next
        removeNodeValue(0, head, values[-n])

        return head

