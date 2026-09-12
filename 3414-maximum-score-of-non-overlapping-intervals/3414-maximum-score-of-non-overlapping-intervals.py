from bisect import bisect_right
from typing import List

class Solution:

    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        sorted_intervals = sorted([(interval[0], interval[1], interval[2], idx) for idx, interval in enumerate(intervals)], key=lambda x: x[0])
        n = len(intervals)
        start_times = [x[0] for x in sorted_intervals]
        next_indices = [bisect_right(start_times, x[1]) for x in sorted_intervals]
        dp = [(0, ())] * ((n + 1) * 5)
        for i in range(n - 1, -1, -1):
            start, end, weight, orig_idx = sorted_intervals[i]
            next_idx = next_indices[i]
            i_offset = i * 5
            i_plus_1_offset = (i + 1) * 5
            next_offset = next_idx * 5
            for j in range(1, 5):
                opt1 = dp[i_plus_1_offset + j]
                prev_score, prev_tup = dp[next_offset + j - 1]
                opt2_score = weight + prev_score
                l = len(prev_tup)
                if l == 0:
                    opt2_tup = (orig_idx,)
                elif l == 1:
                    v0 = prev_tup[0]
                    if orig_idx < v0:
                        opt2_tup = (orig_idx, v0)
                    else:
                        opt2_tup = (v0, orig_idx)
                elif l == 2:
                    v0, v1 = prev_tup
                    if orig_idx < v0:
                        opt2_tup = (orig_idx, v0, v1)
                    elif orig_idx < v1:
                        opt2_tup = (v0, orig_idx, v1)
                    else:
                        opt2_tup = (v0, v1, orig_idx)
                else:
                    v0, v1, v2 = prev_tup
                    if orig_idx < v0:
                        opt2_tup = (orig_idx, v0, v1, v2)
                    elif orig_idx < v1:
                        opt2_tup = (v0, orig_idx, v1, v2)
                    elif orig_idx < v2:
                        opt2_tup = (v0, v1, orig_idx, v2)
                    else:
                        opt2_tup = (v0, v1, v2, orig_idx)
                if opt1[0] != opt2_score:
                    dp[i_offset + j] = opt1 if opt1[0] > opt2_score else (opt2_score, opt2_tup)
                else:
                    dp[i_offset + j] = opt1 if opt1[1] < opt2_tup else (opt2_score, opt2_tup)
        return list(dp[4][1])
