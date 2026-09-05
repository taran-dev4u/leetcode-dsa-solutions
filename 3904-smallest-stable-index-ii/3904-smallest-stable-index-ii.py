class Solution:

    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        suf_min = [0] * n
        suf_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            val = nums[i]
            prev_min = suf_min[i + 1]
            suf_min[i] = val if val < prev_min else prev_min
        curr_max = nums[0]
        for i in range(n):
            val = nums[i]
            if val > curr_max:
                curr_max = val
            if curr_max - suf_min[i] <= k:
                return i
        return -1
