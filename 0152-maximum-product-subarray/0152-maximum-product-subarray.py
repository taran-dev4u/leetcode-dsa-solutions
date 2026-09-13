from typing import List

class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = max_prod = min_prod = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            if x < 0:
                max_prod, min_prod = (min_prod, max_prod)
            max_prod = max(x, max_prod * x)
            min_prod = min(x, min_prod * x)
            if max_prod > ans:
                ans = max_prod
        return ans
