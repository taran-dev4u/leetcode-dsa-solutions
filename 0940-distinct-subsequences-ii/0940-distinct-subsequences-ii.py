class Solution:

    def distinctSubseqII(self, s: str) -> int:
        MOD = 1000000007
        end = [0] * 26
        total_sum = 0
        for char in s:
            idx = ord(char) - 97
            added = (total_sum + 1 - end[idx]) % MOD
            total_sum = (total_sum + added) % MOD
            end[idx] = (end[idx] + added) % MOD
        return total_sum
