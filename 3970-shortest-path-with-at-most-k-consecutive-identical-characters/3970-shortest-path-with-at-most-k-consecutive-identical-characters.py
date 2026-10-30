import heapq
from typing import List

class Solution:

    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if n == 1:
            return 0
        same_adj = [[] for _ in range(n)]
        cross_adj = [[] for _ in range(n)]
        for u, v, w in edges:
            if labels[u] == labels[v]:
                same_adj[u].append((v, w))
            else:
                cross_adj[u].append((v, w))
        K = k + 1
        INF = float('inf')
        dist = [INF] * (n * K)
        visited_node = [False] * n
        dist[1] = 0
        pq = [(0, 0, 1)]
        while pq:
            d, u, count = heapq.heappop(pq)
            if u == n - 1:
                return d
            idx = u * K + count
            if d > dist[idx]:
                continue
            if not visited_node[u]:
                visited_node[u] = True
                for v, w in cross_adj[u]:
                    v_idx = v * K + 1
                    new_d = d + w
                    if new_d < dist[v_idx]:
                        dist[v_idx] = new_d
                        heapq.heappush(pq, (new_d, v, 1))
            c_next = count + 1
            if c_next <= k:
                for v, w in same_adj[u]:
                    v_idx = v * K + c_next
                    new_d = d + w
                    if new_d < dist[v_idx]:
                        dist[v_idx] = new_d
                        heapq.heappush(pq, (new_d, v, c_next))
        return -1
