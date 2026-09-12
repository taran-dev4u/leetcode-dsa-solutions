from typing import List

class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != insert_pos:
                    nums[insert_pos], nums[i] = (nums[i], nums[insert_pos])
                insert_pos += 1
