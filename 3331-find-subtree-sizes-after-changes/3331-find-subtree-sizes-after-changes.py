from collections import defaultdict
from typing import List

class Solution:

    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = defaultdict(list)
        ancestors = defaultdict(list)
        new_parent = [0] * n

        def dfs_find(u, depth):
            char_idx = ord(s[u]) - ord('a')
            if ancestors[char_idx]:
                new_parent[u] = ancestors[char_idx][-1]
            else:
                new_parent[u] = parent[u]
            ancestors[char_idx].append(u)
            for v in adj[u]:
                dfs_find(v, depth + 1)
            ancestors[char_idx].pop()
        for i in range(1, n):
            adj[parent[i]].append(i)
        dfs_find(0, 0)
        new_adj = defaultdict(list)
        for i in range(1, n):
            new_adj[new_parent[i]].append(i)
        ans = [0] * n

        def dfs_size(u):
            size = 1
            for v in new_adj[u]:
                size += dfs_size(v)
            ans[u] = size
            return size
        dfs_size(0)
        return ans
