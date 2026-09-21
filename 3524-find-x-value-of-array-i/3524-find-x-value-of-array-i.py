from typing import List

class Solution:

    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        for num in nums:
            val = num % k
            next_dp = [0] * k
            for v, count in enumerate(dp):
                if count:
                    next_dp[v * val % k] += count
            next_dp[val] += 1
            dp = next_dp
            for v, count in enumerate(dp):
                ans[v] += count
        return ans
