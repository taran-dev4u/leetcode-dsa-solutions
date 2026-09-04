from typing import List

class Solution:

    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        sorted_pairs = sorted(((val, i) for i, val in enumerate(nums)))
        ans = [0] * n
        i = 0
        while i < n:
            j = i + 1
            while j < n and sorted_pairs[j][0] - sorted_pairs[j - 1][0] <= limit:
                j += 1
            indices = [sorted_pairs[k][1] for k in range(i, j)]
            indices.sort()
            for k in range(i, j):
                ans[indices[k - i]] = sorted_pairs[k][0]
            i = j
        return ans
