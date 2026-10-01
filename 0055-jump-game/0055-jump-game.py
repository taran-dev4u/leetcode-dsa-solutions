class Solution:

    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        target = len(nums) - 1
        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            if i + num > max_reach:
                max_reach = i + num
            if max_reach >= target:
                return True
        return True
