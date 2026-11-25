from collections import defaultdict, Counter
from typing import List

class Solution:

    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        P = 10 ** 9 + 9
        B = 131
        powers = [1] * (n + 1)
        for i in range(1, n + 1):
            powers[i] = powers[i - 1] * B % P
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = (pref[i] * B + nums[i]) % P

        def get_hash(l, r):
            return (pref[r + 1] - pref[l] * powers[r - l + 1]) % P

        def check(length):
            if length > n:
                return False
            counts = defaultdict(int)
            for i in range(length - 1):
                pass
            for i in range(n - length + 1):
                h = get_hash(i, i + length - 1)
                counts[h] += 1
                if counts[h] == 1:
                    pass
            for h, count in counts.items():
                if count == 1:
                    return True
            return False
        low, high = (1, n)
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
