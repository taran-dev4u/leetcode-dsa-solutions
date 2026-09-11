from typing import List

class Solution:

    def totalNumbers(self, digits: List[int]) -> int:
        digit_counts = [0] * 10
        for d in digits:
            digit_counts[d] += 1
        total_valid = 0
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = num // 10 % 10
            d3 = num % 10
            digit_counts[d1] -= 1
            digit_counts[d2] -= 1
            digit_counts[d3] -= 1
            if digit_counts[d1] >= 0 and digit_counts[d2] >= 0 and (digit_counts[d3] >= 0):
                total_valid += 1
            digit_counts[d1] += 1
            digit_counts[d2] += 1
            digit_counts[d3] += 1
        return total_valid
