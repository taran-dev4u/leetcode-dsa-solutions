from typing import List

class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def can_ship(capacity: int) -> bool:
            current_days = 1
            current_weight = 0
            for w in weights:
                if current_weight + w > capacity:
                    current_days += 1
                    current_weight = w
                else:
                    current_weight += w
            return current_days <= days
        left = max(weights)
        right = sum(weights)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if can_ship(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
