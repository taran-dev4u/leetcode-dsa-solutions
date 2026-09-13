from typing import List

class Solution:

    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        a_ones = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        b_ones = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        if not a_ones or not b_ones:
            return 0
        limit = 2 * n - 1
        counts = [0] * (limit * limit)
        max_overlap = 0
        for r1, c1 in a_ones:
            for r2, c2 in b_ones:
                idx = (r2 - r1 + n - 1) * limit + (c2 - c1 + n - 1)
                counts[idx] += 1
                if counts[idx] > max_overlap:
                    max_overlap = counts[idx]
        return max_overlap
