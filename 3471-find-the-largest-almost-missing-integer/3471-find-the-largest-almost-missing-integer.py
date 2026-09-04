from collections import Counter
from typing import List

class Solution:

    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subarray_counts = Counter()
        for i in range(n - k + 1):
            unique_elements = set(nums[i:i + k])
            for x in unique_elements:
                subarray_counts[x] += 1
        ans = -1
        for x, count in subarray_counts.items():
            if count == 1:
                if x > ans:
                    ans = x
        return ans
