import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        costs = [0] * n
        low, high = [], []
        in_low = [False] * n
        l_size = h_size = l_sum = h_sum = 0

        def prune(h, min_idx):
            while h and h[0][1] <= min_idx:
                heapq.heappop(h)

        for i, val in enumerate(nums):
            if not low or val <= -low[0][0]:
                heapq.heappush(low, (-val, i))
                in_low[i] = True
                l_sum += val
                l_size += 1
            else:
                heapq.heappush(high, (val, i))
                h_sum += val
                h_size += 1

            out_i = i - x
            if out_i >= 0:
                out_v = nums[out_i]
                if in_low[out_i]:
                    l_sum -= out_v
                    l_size -= 1
                else:
                    h_sum -= out_v
                    h_size -= 1
                prune(low, out_i)
                prune(high, out_i)

            while l_size > h_size + 1:
                prune(low, out_i)
                v, idx = heapq.heappop(low)
                v = -v
                in_low[idx] = False
                l_size -= 1
                l_sum -= v
                heapq.heappush(high, (v, idx))
                h_size += 1
                h_sum += v

            while l_size < h_size:
                prune(high, out_i)
                v, idx = heapq.heappop(high)
                in_low[idx] = True
                h_size -= 1
                h_sum -= v
                heapq.heappush(low, (-v, idx))
                l_size += 1
                l_sum += v

            if i >= x - 1:
                prune(low, out_i)
                med = -low[0][0]
                costs[i] = (l_size * med - l_sum) + (h_sum - h_size * med)

        dp = [0] * (n + 1)
        inf = float('inf')
        for step in range(1, k + 1):
            next_dp = [inf] * (n + 1)
            for i in range(step * x, n + 1):
                next_dp[i] = min(next_dp[i - 1], dp[i - x] + costs[i - 1])
            dp = next_dp

        return dp[n]