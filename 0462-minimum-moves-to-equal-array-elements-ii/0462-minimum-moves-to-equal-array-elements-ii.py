class Solution:

    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        return sum((nums[~i] - nums[i] for i in range(n // 2)))
