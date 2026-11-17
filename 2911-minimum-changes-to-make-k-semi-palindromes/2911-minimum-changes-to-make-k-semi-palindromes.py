class Solution:

    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        divisors = [[] for _ in range(n + 1)]
        for d in range(1, n):
            for L in range(2 * d, n + 1, d):
                divisors[L].append(d)
        cost = [[0] * (n + 1) for _ in range(n)]
        for L in range(2, n + 1):
            divs = divisors[L]
            for i in range(n - L + 1):
                j = i + L
                min_c = float('inf')
                for d in divs:
                    c = 0
                    M = L // d
                    for g in range(d):
                        left = i + g
                        right = i + g + (M - 1) * d
                        while left < right:
                            if s[left] != s[right]:
                                c += 1
                            left += d
                            right -= d
                    if c < min_c:
                        min_c = c
                cost[i][j] = min_c
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for p in range(1, k + 1):
            next_dp = [float('inf')] * (n + 1)
            for j in range(2 * p, n + 1):
                for i in range(2 * (p - 1), j - 1):
                    val = dp[i] + cost[i][j]
                    if val < next_dp[j]:
                        next_dp[j] = val
            dp = next_dp
        return dp[n]
