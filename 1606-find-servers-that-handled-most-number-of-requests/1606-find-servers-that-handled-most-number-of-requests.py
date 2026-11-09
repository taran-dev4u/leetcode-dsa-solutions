import heapq
from bisect import bisect_left, insort

class Solution:

    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = []
        available = list(range(k))
        counts = [0] * k
        for i, (arr_time, l) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= arr_time:
                _, server = heapq.heappop(busy)
                insort(available, server)
            if not available:
                continue
            start = i % k
            idx = bisect_left(available, start)
            if idx == len(available):
                idx = 0
            server = available.pop(idx)
            heapq.heappush(busy, (arr_time + l, server))
            counts[server] += 1
        max_requests = max(counts)
        return [i for i, c in enumerate(counts) if c == max_requests]
