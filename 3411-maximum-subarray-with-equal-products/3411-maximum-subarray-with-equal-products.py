from typing import List
import math

class Solution:

    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        for i in range(n):
            current_prod = 1
            current_gcd = nums[i]
            current_lcm = nums[i]
            for j in range(i, n):
                x = nums[j]
                current_prod *= x
                current_gcd = math.gcd(current_gcd, x)
                current_lcm = current_lcm * x // math.gcd(current_lcm, x)
                if current_prod > 10 ** 14:
                    break
                if current_prod == current_lcm * current_gcd:
                    max_len = max(max_len, j - i + 1)
        return max_len
