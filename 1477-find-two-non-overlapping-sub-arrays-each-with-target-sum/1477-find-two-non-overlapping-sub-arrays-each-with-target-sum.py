from typing import List

class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        ans = float('inf')
        left = 0
        current_sum = 0
        for right in range(n):
            current_sum += arr[right]
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
            if current_sum == target:
                curr_len = right - left + 1
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, curr_len + min_len[left - 1])
                min_len[right] = min(min_len[right - 1] if right > 0 else float('inf'), curr_len)
            else:
                min_len[right] = min_len[right - 1] if right > 0 else float('inf')
        return ans if ans != float('inf') else -1
