class Solution:

    def countCommas(self, n: int) -> int:
        total_commas = 0
        k = 1
        while True:
            lower = 10 ** (3 * k)
            if lower > n:
                break
            upper = 10 ** (3 * (k + 1)) - 1
            limit = min(n, upper)
            count = limit - lower + 1
            total_commas += k * count
            k += 1
        return total_commas
