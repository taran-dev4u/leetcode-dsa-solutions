class Solution:

    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        i = 0
        n = len(intervals)
        new_start, new_end = newInterval
        while i < n and intervals[i][1] < new_start:
            result.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        result.append([new_start, new_end])
        while i < n:
            result.append(intervals[i])
            i += 1
        return result
