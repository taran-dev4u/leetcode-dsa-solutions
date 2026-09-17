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
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        val = sign * res
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        if val < INT_MIN:
            return INT_MIN
        if val > INT_MAX:
            return INT_MAX
        return val
