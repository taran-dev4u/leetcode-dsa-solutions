from typing import List

class Solution:

    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda item: item[1])
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        counts = [0] * (n + 1)
        active_servers = 0
        left = 0
        right = 0
        m = len(logs)
        ans = [0] * len(queries)
        for idx, q in sorted_queries:
            while right < m and logs[right][1] <= q:
                srv = logs[right][0]
                if counts[srv] == 0:
                    active_servers += 1
                counts[srv] += 1
                right += 1
            while left < right and logs[left][1] < q - x:
                srv = logs[left][0]
                counts[srv] -= 1
                if counts[srv] == 0:
                    active_servers -= 1
                left += 1
            ans[idx] = n - active_servers
        return ans
