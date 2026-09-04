from typing import List

class Solution:

    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        min_idx = 0
        max_idx = 0
        for idx, val in enumerate(nums):
            if val < nums[min_idx]:
                min_idx = idx
            if val > nums[max_idx]:
                max_idx = idx
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)
        opt1 = j + 1
        opt2 = n - i
        opt3 = i + 1 + (n - j)
        return min(opt1, opt2, opt3)
