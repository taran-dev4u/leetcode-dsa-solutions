from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        if k == 1:
            ans = []
            for idx, val, start_i, xi in queries:
                nums[idx] = val
                ans.append(n - start_i if xi == 0 else 0)
            return ans

        size = 1
        while size < n:
            size <<= 1

        tree_prod = [1] * (2 * size)
        tree_count = [[[0] * k for _ in range(k)] for _ in range(2 * size)]

        for i in range(n):
            node = size + i
            val = nums[i] % k
            tree_prod[node] = val
            for r1 in range(k):
                tree_count[node][r1][(r1 * val) % k] = 1

        for node in range(size - 1, 0, -1):
            left = 2 * node
            right = left + 1
            l_prod = tree_prod[left]
            tree_prod[node] = (l_prod * tree_prod[right]) % k
            tc = tree_count[node]
            lc = tree_count[left]
            rc = tree_count[right]
            for r1 in range(k):
                rem_r = (r1 * l_prod) % k
                tc_r1 = tc[r1]
                lc_r1 = lc[r1]
                rc_rem = rc[rem_r]
                for r2 in range(k):
                    tc_r1[r2] = lc_r1[r2] + rc_rem[r2]

        ans = []
        for idx, val, start_i, xi in queries:
            node = size + idx
            v = val % k
            tree_prod[node] = v
            tc = tree_count[node]
            for r1 in range(k):
                for r2 in range(k):
                    tc[r1][r2] = 0
                tc[r1][(r1 * v) % k] = 1
            node >>= 1
            while node:
                left = 2 * node
                right = left + 1
                l_prod = tree_prod[left]
                tree_prod[node] = (l_prod * tree_prod[right]) % k
                tc = tree_count[node]
                lc = tree_count[left]
                rc = tree_count[right]
                for r1 in range(k):
                    rem_r = (r1 * l_prod) % k
                    tc_r1 = tc[r1]
                    lc_r1 = lc[r1]
                    rc_rem = rc[rem_r]
                    for r2 in range(k):
                        tc_r1[r2] = lc_r1[r2] + rc_rem[r2]
                node >>= 1

            l = size + start_i
            r = size + n
            nodes = []
            right_nodes = []
            while l < r:
                if l & 1:
                    nodes.append(l)
                    l += 1
                if r & 1:
                    r -= 1
                    right_nodes.append(r)
                l >>= 1
                r >>= 1
            nodes.extend(reversed(right_nodes))

            total_matches = 0
            cur_rem = 1 % k
            for nd in nodes:
                total_matches += tree_count[nd][cur_rem][xi]
                cur_rem = (cur_rem * tree_prod[nd]) % k
            ans.append(total_matches)

        return ans
