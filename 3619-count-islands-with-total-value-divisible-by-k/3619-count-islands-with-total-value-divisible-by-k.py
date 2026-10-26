from typing import List

class Solution:

    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = (len(grid), len(grid[0]))
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    total_sum = grid[r][c]
                    grid[r][c] = 0
                    stack = [(r, c)]
                    while stack:
                        cr, cc = stack.pop()
                        if cr > 0 and grid[cr - 1][cc] > 0:
                            total_sum += grid[cr - 1][cc]
                            grid[cr - 1][cc] = 0
                            stack.append((cr - 1, cc))
                        if cr + 1 < m and grid[cr + 1][cc] > 0:
                            total_sum += grid[cr + 1][cc]
                            grid[cr + 1][cc] = 0
                            stack.append((cr + 1, cc))
                        if cc > 0 and grid[cr][cc - 1] > 0:
                            total_sum += grid[cr][cc - 1]
                            grid[cr][cc - 1] = 0
                            stack.append((cr, cc - 1))
                        if cc + 1 < n and grid[cr][cc + 1] > 0:
                            total_sum += grid[cr][cc + 1]
                            grid[cr][cc + 1] = 0
                            stack.append((cr, cc + 1))
                    if total_sum % k == 0:
                        ans += 1
        return ans
