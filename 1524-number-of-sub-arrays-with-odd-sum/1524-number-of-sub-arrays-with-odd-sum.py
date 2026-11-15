class Solution:

    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        odd_count = 0
        even_count = 1
        parity = 0
        ans = 0
        for x in arr:
            parity ^= x & 1
            if parity:
                ans += even_count
                odd_count += 1
            else:
                ans += odd_count
                even_count += 1
        return ans % MOD
