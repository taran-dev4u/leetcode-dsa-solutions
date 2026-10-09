class Solution:

    def minInsertions(self, s: str) -> int:
        ans = 0
        left = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                left += 1
                i += 1
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                else:
                    ans += 1
                    i += 1
                if left > 0:
                    left -= 1
                else:
                    ans += 1
        ans += left * 2
        return ans
