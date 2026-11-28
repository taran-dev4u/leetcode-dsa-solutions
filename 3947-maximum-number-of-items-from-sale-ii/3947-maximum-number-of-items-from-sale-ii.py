from typing import List
from collections import defaultdict

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        cheapest = min(p for f, p in items)
        max_factor = max(f for f, p in items)

        cnt = [0] * (max_factor + 1)
        for f, p in items:
            cnt[f] += 1

        multiples = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if cnt[f] > 0:
                for m in range(f, max_factor + 1, f):
                    multiples[f] += cnt[m]

        cost_count = defaultdict(int)
        threshold = 2 * cheapest
        for f, p in items:
            free_copies = multiples[f] - 1
            if free_copies > 0 and p <= threshold:
                cost_count[p] += free_copies

        total = 0
        for cost in sorted(cost_count):
            count = cost_count[cost]
            include = min(count, budget // cost)
            total += 2 * include
            budget -= include * cost
            if budget < cost:
                break

        total += budget // cheapest
        return total
