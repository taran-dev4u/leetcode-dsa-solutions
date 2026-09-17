class Solution:

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        T = '^#' + '#'.join(s) + '#$'
        n = len(T)
        P = [0] * n
        C = 0
        R = 0
        for i in range(1, n - 1):
            i_mirror = 2 * C - i
            if R > i:
                P[i] = min(R - i, P[i_mirror])
            else:
                P[i] = 0
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            if i + P[i] > R:
                C = i
                R = i + P[i]
        max_len = 0
        center_index = 0
        for i in range(1, n - 1):
            if P[i] > max_len:
                max_len = P[i]
                center_index = i
        start = (center_index - 1 - max_len) // 2
        return s[start:start + max_len]
