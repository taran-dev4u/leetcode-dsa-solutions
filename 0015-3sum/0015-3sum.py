class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            val = nums[i]
            if val > 0:
                break
            if i > 0 and val == nums[i - 1]:
                continue
            if val + nums[i + 1] + nums[i + 2] > 0:
                break
            if val + nums[-1] + nums[-2] < 0:
                continue
            left, right = (i + 1, n - 1)
            while left < right:
                total = val + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([val, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res
