class Solution:

    def minCost(self, grid: list[list[int]]) -> int:
        m, n = (len(grid), len(grid[0]))
        dp = [set() for _ in range(n)]
        curr = 0
        for c in range(n):
            curr ^= grid[0][c]
            dp[c].add(curr)
        for r in range(1, m):
            dp[0] = {x ^ grid[r][0] for x in dp[0]}
            for c in range(1, n):
                val = grid[r][c]
                dp[c] = {x ^ val for x in dp[c] | dp[c - 1]}
        return min(dp[-1])
