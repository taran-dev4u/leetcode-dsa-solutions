from typing import List

class Solution:

    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        b1 = [0] * (n + 2)
        b2 = [0] * (n + 2)

        def add_point(b, idx, val):
            while idx <= n + 1:
                b[idx] = (b[idx] + val) % MOD
                idx += idx & -idx

        def query_point(b, idx):
            s = 0
            while idx > 0:
                s = (s + b[idx]) % MOD
                idx -= idx & -idx
            return s

        def add_range(l, r, val):
            add_point(b1, l, val)
            add_point(b1, r + 1, -val)
            add_point(b2, l, val * (l - 1))
            add_point(b2, r + 1, -val * r)

        def prefix_sum(idx):
            return (query_point(b1, idx) * idx - query_point(b2, idx)) % MOD

        def query_range(l, r):
            return (prefix_sum(r) - prefix_sum(l - 1)) % MOD
        ans = 0
        cur_s2 = 0
        last_pos = [-1] * 100001
        for j, v in enumerate(nums):
            p = last_pos[v]
            l = p + 2
            r = j + 1
            q_sum = query_range(l, r)
            delta = (2 * q_sum + (j - p)) % MOD
            cur_s2 = (cur_s2 + delta) % MOD
            ans = (ans + cur_s2) % MOD
            add_range(l, r, 1)
            last_pos[v] = j
        return ans
