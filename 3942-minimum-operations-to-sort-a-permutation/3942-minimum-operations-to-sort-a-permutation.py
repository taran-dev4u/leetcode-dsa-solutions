from typing import List

class Solution:

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        c = nums[0]
        is_type1 = all(((x - i) % n == c for i, x in enumerate(nums)))
        k = (n - 1 - nums[0]) % n
        target_sum = (n - 1 - k) % n
        is_type2 = all(((x + i) % n == target_sum for i, x in enumerate(nums)))
        ans = float('inf')
        if is_type1:
            ans = min(ans, (n - c) % n, c + 2)
        if is_type2:
            ans = min(ans, (n - k) % n + 1, k + 1)
        return ans if ans != float('inf') else -1
