class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        seen = []

        def dfs(node, remove, prev):
            nonlocal seen

            if not node:
                return

            if node == remove:
                if prev:
                    prev.next = node.next
            else:
                seen.append(node)

            dfs(node.next, remove, node)

        dfs(head, None, None)

        remove = seen[-n]

        if head is remove:
            return head.next

        dfs(head, remove, None)

        return head