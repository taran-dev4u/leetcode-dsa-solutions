import sys

class Solution:

    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        sys.setrecursionlimit(300000)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        LOG = 17
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 1
        order = []
        stack = [(0, -1)]
        visited_adj = [0] * n
        depth[0] = 0
        while stack:
            u, p = stack[-1]
            if visited_adj[u] == 0:
                tin[u] = timer
                timer += 1
                up[u][0] = p if p != -1 else 0
                for j in range(1, LOG):
                    up[u][j] = up[up[u][j - 1]][j - 1]
            if visited_adj[u] < len(adj[u]):
                v = adj[u][visited_adj[u]]
                visited_adj[u] += 1
                if v != p:
                    depth[v] = depth[u] + 1
                    stack.append((v, u))
            else:
                tout[u] = timer - 1
                stack.pop()

        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = (v, u)
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if diff >> j & 1:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]
        bit = [0] * (n + 2)

        def bit_update(idx: int, val: int) -> None:
            while idx <= n + 1:
                bit[idx] ^= val
                idx += idx & -idx

        def bit_query(idx: int) -> int:
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & -idx
            return res
        s_chars = list(s)
        for i in range(n):
            val = 1 << ord(s_chars[i]) - 97
            bit_update(tin[i], val)
            bit_update(tout[i] + 1, val)
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == 'update':
                u = int(parts[1])
                c = parts[2]
                old_c = s_chars[u]
                if old_c != c:
                    diff = 1 << ord(old_c) - 97 ^ 1 << ord(c) - 97
                    s_chars[u] = c
                    bit_update(tin[u], diff)
                    bit_update(tout[u] + 1, diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                mask_u = bit_query(tin[u])
                mask_v = bit_query(tin[v])
                lca_char_mask = 1 << ord(s_chars[lca]) - 97
                path_mask = mask_u ^ mask_v ^ lca_char_mask
                ans.append(path_mask & path_mask - 1 == 0)
        return ans
