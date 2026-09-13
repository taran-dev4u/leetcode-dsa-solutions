from typing import List

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            if current_sum < 0:
                current_sum = x
            else:
                current_sum += x
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum
