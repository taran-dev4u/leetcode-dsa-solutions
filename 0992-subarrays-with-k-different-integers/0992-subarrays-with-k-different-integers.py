class Solution:

    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:

        def atMost(k: int) -> int:
            if k == 0:
                return 0
            freq = [0] * (len(nums) + 1)
            left = 0
            distinct = 0
            ans = 0
            for right, x in enumerate(nums):
                if freq[x] == 0:
                    distinct += 1
                freq[x] += 1
                while distinct > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        distinct -= 1
                    left += 1
                ans += right - left + 1
            return ans
        return atMost(k) - atMost(k - 1)
