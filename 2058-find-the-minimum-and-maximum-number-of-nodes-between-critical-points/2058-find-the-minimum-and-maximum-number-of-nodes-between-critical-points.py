class Solution:

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or (not head.next.next):
            return [-1, -1]
        first_critical = -1
        prev_critical = -1
        min_dist = float('inf')
        prev = head
        curr = head.next
        curr_idx = 1
        while curr.next:
            nxt = curr.next
            if curr.val > prev.val and curr.val > nxt.val or (curr.val < prev.val and curr.val < nxt.val):
                if first_critical == -1:
                    first_critical = curr_idx
                else:
                    min_dist = min(min_dist, curr_idx - prev_critical)
                prev_critical = curr_idx
            prev = curr
            curr = nxt
            curr_idx += 1
        if first_critical == prev_critical:
            return [-1, -1]
        return [min_dist, prev_critical - first_critical]
