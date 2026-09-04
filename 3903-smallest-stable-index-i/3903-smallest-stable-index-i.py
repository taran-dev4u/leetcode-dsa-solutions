class Solution:

    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        min_suffix = [0] * n
        min_suffix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] < min_suffix[i + 1]:
                min_suffix[i] = nums[i]
            else:
                min_suffix[i] = min_suffix[i + 1]
        running_max = nums[0]
        for i in range(n):
            if nums[i] > running_max:
                running_max = nums[i]
            if running_max - min_suffix[i] <= k:
                return i
        return -1
