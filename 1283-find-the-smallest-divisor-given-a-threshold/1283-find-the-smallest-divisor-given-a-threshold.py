import math
from typing import List

class Solution:

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def get_sum(divisor: int) -> int:
            return sum(((num + divisor - 1) // divisor for num in nums))
        left, right = (1, max(nums))
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if get_sum(mid) <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
