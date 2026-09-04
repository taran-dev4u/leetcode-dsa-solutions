from typing import List

class Solution:

    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        idx = [i for i, c in enumerate(s) if c == '1']
        if len(idx) < k:
            return ''
        min_len = len(s) + 1
        candidates = []
        for i in range(len(idx) - k + 1):
            length = idx[i + k - 1] - idx[i] + 1
            if length < min_len:
                min_len = length
                candidates = [s[idx[i]:idx[i + k - 1] + 1]]
            elif length == min_len:
                candidates.append(s[idx[i]:idx[i + k - 1] + 1])
        return min(candidates)
