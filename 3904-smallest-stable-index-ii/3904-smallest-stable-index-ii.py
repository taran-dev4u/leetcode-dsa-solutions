class Solution:

    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        suff_min = [0] * n
        curr_min = nums[-1]
        suff_min[-1] = curr_min
        for i in range(n - 2, -1, -1):
            val = nums[i]
            if val < curr_min:
                curr_min = val
            suff_min[i] = curr_min
        pref_max = nums[0]
        for i, val in enumerate(nums):
            if val > pref_max:
                pref_max = val
            if pref_max - suff_min[i] <= k:
                return i
        return -1
