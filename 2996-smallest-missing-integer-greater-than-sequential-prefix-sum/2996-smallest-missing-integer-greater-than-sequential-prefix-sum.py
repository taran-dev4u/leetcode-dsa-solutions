from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        s = nums[0]
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                s += nums[i]
            else:
                break
        
        nums_set = set(nums)
        x = s
        while x in nums_set:
            x += 1
        return x
