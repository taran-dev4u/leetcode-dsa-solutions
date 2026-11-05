from bisect import bisect_left

class Solution:

    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        ans = 0
        n = len(arr2)
        for x in arr1:
            idx = bisect_left(arr2, x - d)
            if idx == n or arr2[idx] > x + d:
                ans += 1
        return ans
