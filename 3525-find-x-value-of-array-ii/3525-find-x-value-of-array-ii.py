from typing import List

class Solution:

    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        N = len(nums)
        mult_table = [[i * j % k for j in range(k)] for i in range(k)]
        tree = [None] * (2 * N)
        curr_mods = [x % k for x in nums]
        for i in range(N):
            val = curr_mods[i]
            counts = [0] * k
            counts[val] = 1
            tree[N + i] = [val, counts]

        def merge(left, right):
            lp, lc = left
            rp, rc = right
            tp = mult_table[lp][rp]
            nc = lc[:]
            row = mult_table[lp]
            for r in range(k):
                nc[row[r]] += rc[r]
            return [tp, nc]
        for i in range(N - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])
        ans = []
        identity = [1 % k, [0] * k]
        tree_local = tree
        curr_mods_local = curr_mods
        merge_local = merge
        ans_append = ans.append
        for index, value, start, x in queries:
            val = value % k
            if curr_mods_local[index] != val:
                curr_mods_local[index] = val
                idx = index + N
                counts = [0] * k
                counts[val] = 1
                tree_local[idx] = [val, counts]
                idx >>= 1
                while idx > 0:
                    tree_local[idx] = merge_local(tree_local[2 * idx], tree_local[2 * idx + 1])
                    idx >>= 1
            l = start + N
            r = N + N
            res_l = identity
            res_r = identity
            while l < r:
                if l & 1:
                    res_l = merge_local(res_l, tree_local[l])
                    l += 1
                if r & 1:
                    r -= 1
                    res_r = merge_local(tree_local[r], res_r)
                l >>= 1
                r >>= 1
            res = merge_local(res_l, res_r)
            ans_append(res[1][x])
        return ans
