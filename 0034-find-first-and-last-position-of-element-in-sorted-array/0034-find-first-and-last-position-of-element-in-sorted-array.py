from typing import List
import bisect

class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        if left < len(nums) and nums[left] == target:
            right = bisect.bisect_right(nums, target)
            return [left, right - 1]
        return [-1, -1]
