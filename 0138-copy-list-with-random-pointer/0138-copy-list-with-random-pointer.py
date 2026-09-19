class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        curr = head
        dummy = Node(0)
        copy_curr = dummy
        while curr:
            copy = curr.next
            next_original = copy.next
            copy_curr.next = copy
            copy_curr = copy
            curr.next = next_original
            curr = next_original
        return dummy.next
