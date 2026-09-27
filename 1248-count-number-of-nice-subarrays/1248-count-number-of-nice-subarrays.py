class Solution:

    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        count = [0] * (len(nums) + 1)
        count[0] = 1
        curr = 0
        ans = 0
        for x in nums:
            curr += x & 1
            if curr >= k:
                ans += count[curr - k]
            count[curr] += 1
        return ans
