from typing import List

class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        total_sum = 0
        for r in range(len(nums)):
            total_sum += nums[r]
            if nums[r] * (r - l + 1) - total_sum > k:
                total_sum -= nums[l]
                l += 1
        return len(nums) - l
