class Solution:

    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        board = [0] * n

        def backtrack(row: int, cols: int, diag1: int, diag2: int):
            if row == n:
                res = []
                for c in board:
                    row_str = ['.'] * n
                    row_str[c] = 'Q'
                    res.append(''.join(row_str))
                ans.append(res)
                return
            available = (1 << n) - 1 & ~(cols | diag1 | diag2)
            while available:
                p = available & -available
                col = p.bit_length() - 1
                board[row] = col
                backtrack(row + 1, cols | p, (diag1 | p) << 1, (diag2 | p) >> 1)
                available &= available - 1
        backtrack(0, 0, 0, 0)
        return ans
