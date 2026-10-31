from typing import List

class Solution:

    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = (len(grid), len(grid[0]))
        MOD = 10 ** 9 + 7
        dest_R = [[None] * n for _ in range(m)]
        dest_D = [[None] * n for _ in range(m)]
        dp = [[0] * n for _ in range(m)]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 0:
                    dest_R[r][c] = (r, c)
                    dest_D[r][c] = (r, c)
                else:
                    if r + 1 < m:
                        dest_R[r][c] = dest_D[r + 1][c]
                    if c + 1 < n:
                        dest_D[r][c] = dest_R[r][c + 1]
        dp[m - 1][n - 1] = 1
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 0:
                    res = dp[r][c]
                    if c + 1 < n:
                        target = dest_R[r][c + 1]
                        if target:
                            res = (res + dp[target[0]][target[1]]) % MOD
                    if r + 1 < m:
                        target = dest_D[r + 1][c]
                        if target:
                            res = (res + dp[target[0]][target[1]]) % MOD
                    dp[r][c] = res
        return dp[0][0]
