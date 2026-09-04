class Solution:

    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        prefix_max = [0] * n
        current_max = nums[0]
        for i in range(n):
            if nums[i] > current_max:
                current_max = nums[i]
            prefix_max[i] = current_max
        suffix_min = [0] * n
        current_min = nums[-1]
        for i in range(n - 1, -1, -1):
            if nums[i] < current_min:
                current_min = nums[i]
            suffix_min[i] = current_min
        for i in range(n):
            if prefix_max[i] - suffix_min[i] <= k:
                return i
        return -1
