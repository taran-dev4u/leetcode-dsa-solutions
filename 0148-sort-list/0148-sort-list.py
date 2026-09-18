class Solution:

    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        dummy = ListNode(0)
        dummy.next = head

        def split(head: ListNode | None, step: int) -> ListNode | None:
            curr = head
            for _ in range(step - 1):
                if not curr:
                    break
                curr = curr.next
            if not curr:
                return None
            next_head = curr.next
            curr.next = None
            return next_head
        merge_dummy = ListNode(0)

        def merge(l1: ListNode | None, l2: ListNode | None) -> tuple[ListNode, ListNode]:
            tail = merge_dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            while tail.next:
                tail = tail.next
            return (merge_dummy.next, tail)
        step = 1
        while step < length:
            curr = dummy.next
            prev = dummy
            while curr:
                l1 = curr
                l2 = split(l1, step)
                curr = split(l2, step)
                merged_head, merged_tail = merge(l1, l2)
                prev.next = merged_head
                prev = merged_tail
            step *= 2
        return dummy.next
