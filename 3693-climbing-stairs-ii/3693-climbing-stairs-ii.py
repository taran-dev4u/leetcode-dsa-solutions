from typing import List

class Solution:

    def climbStairs(self, n: int, costs: List[int]) -> int:
        d0, d1, d2 = (float('inf'), float('inf'), 0)
        for c in costs:
            d0, d1, d2 = (d1, d2, c + min(d2 + 1, d1 + 4, d0 + 9))
        return d2
