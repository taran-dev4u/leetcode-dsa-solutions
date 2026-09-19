class Solution:

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = [[]]
        end_idx = 0
        for i in range(len(nums)):
            start_idx = 0
            if i > 0 and nums[i] == nums[i - 1]:
                start_idx = end_idx
            end_idx = len(res)
            for j in range(start_idx, end_idx):
                res.append(res[j] + [nums[i]])
        return res
