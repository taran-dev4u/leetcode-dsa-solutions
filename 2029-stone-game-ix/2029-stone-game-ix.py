from typing import List

class Solution:

    def stoneGameIX(self, stones: List[int]) -> bool:
        c = [0, 0, 0]
        for stone in stones:
            c[stone % 3] += 1
        c0, c1, c2 = (c[0], c[1], c[2])
        if c0 % 2 == 0:
            return min(c1, c2) > 0
        return abs(c1 - c2) > 2
