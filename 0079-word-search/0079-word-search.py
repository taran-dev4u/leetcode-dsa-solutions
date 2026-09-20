from collections import Counter

class Solution:

    def exist(self, board: list[list[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        L = len(word)
        if L > R * C:
            return False
        board_counts = Counter((char for row in board for char in row))
        word_counts = Counter(word)
        for char, count in word_counts.items():
            if board_counts[char] < count:
                return False
        if board_counts[word[0]] > board_counts[word[-1]]:
            word = word[::-1]

        def dfs(r: int, c: int, k: int) -> bool:
            if k == L:
                return True
            if r < 0 or r >= R or c < 0 or (c >= C) or (board[r][c] != word[k]):
                return False
            temp = board[r][c]
            board[r][c] = '#'
            found = dfs(r + 1, c, k + 1) or dfs(r - 1, c, k + 1) or dfs(r, c + 1, k + 1) or dfs(r, c - 1, k + 1)
            board[r][c] = temp
            return found
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False
