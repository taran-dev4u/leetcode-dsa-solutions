class Solution:

    def closedIsland(self, grid: list[list[int]]) -> int:
        R, C = (len(grid), len(grid[0]))

        def dfs(r, c):
            stack = [(r, c)]
            grid[r][c] = 1
            while stack:
                curr_r, curr_c = stack.pop()
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr, nc = (curr_r + dr, curr_c + dc)
                    if 0 <= nr < R and 0 <= nc < C and (grid[nr][nc] == 0):
                        grid[nr][nc] = 1
                        stack.append((nr, nc))
        for r in range(R):
            if grid[r][0] == 0:
                dfs(r, 0)
            if grid[r][C - 1] == 0:
                dfs(r, C - 1)
        for c in range(C):
            if grid[0][c] == 0:
                dfs(0, c)
            if grid[R - 1][c] == 0:
                dfs(R - 1, c)
        ans = 0
        for r in range(1, R - 1):
            for c in range(1, C - 1):
                if grid[r][c] == 0:
                    ans += 1
                    dfs(r, c)
        return ans
