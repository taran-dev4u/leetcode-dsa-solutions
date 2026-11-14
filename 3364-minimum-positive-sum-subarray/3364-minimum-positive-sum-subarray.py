from typing import List

class Solution:

    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        ans = float('inf')
        for k in range(l, r + 1):
            for i in range(n - k + 1):
                s = pref[i + k] - pref[i]
                if 0 < s < ans:
                    ans = s
        return ans if ans != float('inf') else -1
