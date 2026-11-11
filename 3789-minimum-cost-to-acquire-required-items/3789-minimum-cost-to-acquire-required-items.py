class Solution:

    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        m = min(need1, need2)
        M = max(need1, need2)
        ans0 = need1 * cost1 + need2 * cost2
        ans1 = m * costBoth + (need1 - m) * cost1 + (need2 - m) * cost2
        ans2 = M * costBoth
        return min(ans0, ans1, ans2)
