from collections import defaultdict

class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        n, m = (len(s), len(t))
        if n < m:
            return 0
        dp = [0] * (m + 1)
        dp[0] = 1
        pos = defaultdict(list)
        for i, char in enumerate(t):
            pos[char].append(i)
        for char in pos:
            pos[char].reverse()
        pos_get = pos.get
        for char in s:
            indices = pos_get(char)
            if indices:
                for idx in indices:
                    dp[idx + 1] += dp[idx]
        return dp[m]
