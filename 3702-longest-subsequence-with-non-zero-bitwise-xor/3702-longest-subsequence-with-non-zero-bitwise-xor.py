from typing import List

class Solution:

    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        all_zeros = True
        for x in nums:
            total_xor ^= x
            if x != 0:
                all_zeros = False
        if all_zeros:
            return 0
        if total_xor != 0:
            return len(nums)
        return len(nums) - 1
