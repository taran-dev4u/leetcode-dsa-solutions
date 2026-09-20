class Solution:

    def solveSudoku(self, board: list[list[str]]) -> None:
        BOX_INDEX = [[r // 3 * 3 + c // 3 for c in range(9)] for r in range(9)]
        POPCOUNT = [bin(i).count('1') for i in range(512)]
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty_cells = []
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    digit = int(val) - 1
                    mask = 1 << digit
                    rows[r] |= mask
                    cols[c] |= mask
                    boxes[BOX_INDEX[r][c]] |= mask
                else:
                    empty_cells.append((r, c))
        n_empty = len(empty_cells)

        def backtrack(index: int) -> bool:
            if index == n_empty:
                return True
            best_idx = index
            min_candidates = 10
            best_mask = 0
            for i in range(index, n_empty):
                r, c = empty_cells[i]
                b = BOX_INDEX[r][c]
                mask = ~(rows[r] | cols[c] | boxes[b]) & 511
                candidates_count = POPCOUNT[mask]
                if candidates_count < min_candidates:
                    min_candidates = candidates_count
                    best_idx = i
                    best_mask = mask
                    if min_candidates == 0:
                        break
                    if min_candidates == 1:
                        break
            if min_candidates == 0:
                return False
            empty_cells[index], empty_cells[best_idx] = (empty_cells[best_idx], empty_cells[index])
            r, c = empty_cells[index]
            b = BOX_INDEX[r][c]
            mask = best_mask
            while mask > 0:
                lowbit = mask & -mask
                mask ^= lowbit
                digit_idx = lowbit.bit_length() - 1
                board[r][c] = str(digit_idx + 1)
                rows[r] |= lowbit
                cols[c] |= lowbit
                boxes[b] |= lowbit
                if backtrack(index + 1):
                    return True
                rows[r] ^= lowbit
                cols[c] ^= lowbit
                boxes[b] ^= lowbit
            board[r][c] = '.'
            return False
        backtrack(0)
