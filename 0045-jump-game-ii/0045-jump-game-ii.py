class Solution:

    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        jumps = 0
        current_end = 0
        furthest = 0
        for i in range(n - 1):
            if i + nums[i] > furthest:
                furthest = i + nums[i]
            if i == current_end:
                jumps += 1
                current_end = furthest
                if current_end >= n - 1:
                    break
        return jumps
