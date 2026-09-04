from typing import List
import math

class Solution:

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins = sorted(list(set(coins)))
        filtered_coins = []
        for c in coins:
            if not any((c % item == 0 for item in filtered_coins)):
                filtered_coins.append(c)
        coins = filtered_coins
        n = len(coins)
        max_val = min(coins) * k
        subsets = []

        def dfs(idx: int, current_lcm: int, count: int):
            if idx == n:
                if count > 0:
                    sign = 1 if count % 2 == 1 else -1
                    subsets.append((current_lcm, sign))
                return
            dfs(idx + 1, current_lcm, count)
            if current_lcm == 0:
                next_lcm = coins[idx]
            else:
                next_lcm = current_lcm * coins[idx] // math.gcd(current_lcm, coins[idx])
            if next_lcm <= max_val:
                dfs(idx + 1, next_lcm, count + 1)
        dfs(0, 0, 0)
        low = 1
        high = max_val
        ans = max_val
        while low <= high:
            mid = (low + high) // 2
            cnt = 0
            for lcm, sign in subsets:
                cnt += sign * (mid // lcm)
            if cnt >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
