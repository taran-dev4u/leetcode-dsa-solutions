class Solution:

    def countServers(self, grid: list[list[int]]) -> int:
        row_count = [sum(r) for r in grid]
        col_count = [sum(c) for c in zip(*grid)]
        return sum((1 for i, row in enumerate(grid) for j, val in enumerate(row) if val and (row_count[i] > 1 or col_count[j] > 1)))
