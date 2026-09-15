from typing import List

class Solution:

    def splitArray(self, nums: List[int], k: int) -> int:

        def can_split(max_sum: int) -> bool:
            subarrays = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
            return True
        left = max(nums)
        right = sum(nums)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if can_split(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
