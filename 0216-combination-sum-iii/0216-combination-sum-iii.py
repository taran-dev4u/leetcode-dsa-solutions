from itertools import combinations

class Solution:

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        min_sum = k * (k + 1) // 2
        max_sum = k * (19 - k) // 2
        if n < min_sum or n > max_sum:
            return []
        return [list(comb) for comb in combinations(range(1, 10), k) if sum(comb) == n]
