class Solution:

    def countGoodNumbers(self, n: int) -> int:
        MOD = 1000000007
        even_indices = (n + 1) // 2
        odd_indices = n // 2
        return pow(5, even_indices, MOD) * pow(4, odd_indices, MOD) % MOD
