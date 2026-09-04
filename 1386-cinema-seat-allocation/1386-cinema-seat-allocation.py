from collections import defaultdict
from typing import List

class Solution:

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_masks = defaultdict(int)
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                row_masks[r] |= 1 << c - 2
        ans = 2 * (n - len(row_masks))
        for mask in row_masks.values():
            if mask & 15 == 0 and mask & 240 == 0:
                ans += 2
            elif mask & 15 == 0 or mask & 240 == 0 or mask & 60 == 0:
                ans += 1
        return ans
