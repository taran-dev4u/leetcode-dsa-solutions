from typing import List

class Solution:

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        current_len = 0
        for num in nums:
            if num == 1:
                current_len += 1
            else:
                if current_len > max_len:
                    max_len = current_len
                current_len = 0
        if current_len > max_len:
            max_len = current_len
        return max_len
