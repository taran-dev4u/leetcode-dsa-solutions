from collections import deque
from typing import List

class Solution:

    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque()
        cost = 0
        ans = 0
        r = n - 1
        for l in range(n - 1, -1, -1):
            val = nums[l]
            count = 1
            while q and q[0][0] <= val:
                v, c = q.popleft()
                cost += (val - v) * c
                count += c
            q.appendleft([val, count])
            while cost > k:
                cost -= q[-1][0] - nums[r]
                q[-1][1] -= 1
                if q[-1][1] == 0:
                    q.pop()
                r -= 1
            ans += r - l + 1
        return ans
