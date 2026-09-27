class Solution:

    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count = [0] * (len(nums) + 1)
        count[0] = 1
        curr = 0
        ans = 0
        for x in nums:
            curr += x
            if curr >= goal:
                ans += count[curr - goal]
            count[curr] += 1
        return ans
