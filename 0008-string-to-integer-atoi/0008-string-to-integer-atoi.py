class Solution:

    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        res = 0
        while i < n and '0' <= s[i] <= '9':
            res = res * 10 + (ord(s[i]) - 48)
            i += 1
        res *= sign
        INT_MIN, INT_MAX = (-2147483648, 2147483647)
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        return res
