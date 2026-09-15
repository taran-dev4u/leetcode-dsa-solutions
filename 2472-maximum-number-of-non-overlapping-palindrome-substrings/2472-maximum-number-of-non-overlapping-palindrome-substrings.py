from collections import deque

class Solution:

    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        start = 0
        for i in range(n):
            if i - k + 1 >= start:
                sub = s[i - k + 1:i + 1]
                if sub == sub[::-1]:
                    ans += 1
                    start = i + 1
                    continue
            if i - k >= start:
                sub = s[i - k:i + 1]
                if sub == sub[::-1]:
                    ans += 1
                    start = i + 1
                    continue
        return ans
