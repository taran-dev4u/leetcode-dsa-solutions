class Solution:

    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        for _ in range(n + 1):
            if fast is not None:
                fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        if slow.next is not None:
            slow.next = slow.next.next
        return dummy.next
