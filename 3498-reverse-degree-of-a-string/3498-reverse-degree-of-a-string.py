class Solution:

    def reverseDegree(self, s: str) -> int:
        total_sum = 0
        for i, char in enumerate(s):
            rev_alpha_pos = 26 - (ord(char) - 97)
            total_sum += rev_alpha_pos * (i + 1)
        return total_sum
