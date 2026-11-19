import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        m = len(tasks)
        
        available = [(servers[i], i) for i in range(n)]
        heapq.heapify(available)
        
        busy = []
        ans = [0] * m
        current_time = 0
        
        for j in range(m):
            current_time = max(current_time, j)
            
            if not available and busy[0][0] > current_time:
                current_time = busy[0][0]
                
            while busy and busy[0][0] <= current_time:
                free_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))
                
            weight, idx = heapq.heappop(available)
            ans[j] = idx
            
            heapq.heappush(busy, (current_time + tasks[j], weight, idx))
            
        return ans