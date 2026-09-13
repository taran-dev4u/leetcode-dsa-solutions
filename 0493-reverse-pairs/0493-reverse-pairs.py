from typing import List

class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        all_vals = set(nums)
        all_vals.update((2 * x for x in nums))
        sorted_vals = sorted(all_vals)
        rank = {val: i + 1 for i, val in enumerate(sorted_vals)}
        n = len(sorted_vals)
        tree = [0] * (n + 1)
        ans = 0
        for count_inserted, x in enumerate(nums):
            idx = rank[2 * x]
            s = 0
            while idx > 0:
                s += tree[idx]
                idx -= idx & -idx
            ans += count_inserted - s
            idx = rank[x]
            while idx <= n:
                tree[idx] += 1
                idx += idx & -idx
        return ans
