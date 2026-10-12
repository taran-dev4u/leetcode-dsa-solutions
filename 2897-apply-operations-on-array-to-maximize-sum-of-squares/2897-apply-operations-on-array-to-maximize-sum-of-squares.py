from typing import List

class Solution:

    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        bit_counts = [sum((x >> b & 1 for x in nums)) for b in range(30)]
        ans = 0
        for _ in range(k):
            val = 0
            for b in range(30):
                if bit_counts[b] > 0:
                    val |= 1 << b
                    bit_counts[b] -= 1
            ans = (ans + val * val) % MOD
        return ans
