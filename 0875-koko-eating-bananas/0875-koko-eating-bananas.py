import math
from typing import List

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = (1, max(piles))
        ans = right
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid
            if hours <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
