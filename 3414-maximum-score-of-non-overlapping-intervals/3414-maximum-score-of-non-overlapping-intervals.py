import bisect
from typing import List

class Solution:

    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)
        sorted_intervals = sorted(range(N), key=lambda x: intervals[x][0])
        start_times = [intervals[idx][0] for idx in sorted_intervals]
        next_idx = [0] * N
        for i in range(N):
            r_val = intervals[sorted_intervals[i]][1]
            next_idx[i] = bisect.bisect_right(start_times, r_val)

        def insert_sorted(lst, val):
            if not lst:
                return [val]
            n = len(lst)
            if n == 1:
                return [val, lst[0]] if val < lst[0] else [lst[0], val]
            if n == 2:
                if val < lst[0]:
                    return [val, lst[0], lst[1]]
                elif val < lst[1]:
                    return [lst[0], val, lst[1]]
                else:
                    return [lst[0], lst[1], val]
            if n == 3:
                if val < lst[0]:
                    return [val, lst[0], lst[1], lst[2]]
                elif val < lst[1]:
                    return [lst[0], val, lst[1], lst[2]]
                elif val < lst[2]:
                    return [lst[0], lst[1], val, lst[2]]
                else:
                    return [lst[0], lst[1], lst[2], val]
            return lst
        dp_weight_0 = [0] * (N + 1)
        dp_weight_1 = [0] * (N + 1)
        dp_weight_2 = [0] * (N + 1)
        dp_weight_3 = [0] * (N + 1)
        dp_weight_4 = [0] * (N + 1)
        dp_indices_0 = [[] for _ in range(N + 1)]
        dp_indices_1 = [[] for _ in range(N + 1)]
        dp_indices_2 = [[] for _ in range(N + 1)]
        dp_indices_3 = [[] for _ in range(N + 1)]
        dp_indices_4 = [[] for _ in range(N + 1)]
        for i in range(N - 1, -1, -1):
            orig_idx = sorted_intervals[i]
            w_val = intervals[orig_idx][2]
            nxt = next_idx[i]
            w1 = dp_weight_1[i + 1]
            w2 = w_val + dp_weight_0[nxt]
            if w1 > w2:
                dp_weight_1[i] = w1
                dp_indices_1[i] = dp_indices_1[i + 1]
            elif w2 > w1:
                dp_weight_1[i] = w2
                dp_indices_1[i] = insert_sorted(dp_indices_0[nxt], orig_idx)
            else:
                idx1 = dp_indices_1[i + 1]
                idx2 = insert_sorted(dp_indices_0[nxt], orig_idx)
                if idx1 < idx2:
                    dp_weight_1[i] = w1
                    dp_indices_1[i] = idx1
                else:
                    dp_weight_1[i] = w2
                    dp_indices_1[i] = idx2
            w1 = dp_weight_2[i + 1]
            w2 = w_val + dp_weight_1[nxt]
            if w1 > w2:
                dp_weight_2[i] = w1
                dp_indices_2[i] = dp_indices_2[i + 1]
            elif w2 > w1:
                dp_weight_2[i] = w2
                dp_indices_2[i] = insert_sorted(dp_indices_1[nxt], orig_idx)
            else:
                idx1 = dp_indices_2[i + 1]
                idx2 = insert_sorted(dp_indices_1[nxt], orig_idx)
                if idx1 < idx2:
                    dp_weight_2[i] = w1
                    dp_indices_2[i] = idx1
                else:
                    dp_weight_2[i] = w2
                    dp_indices_2[i] = idx2
            w1 = dp_weight_3[i + 1]
            w2 = w_val + dp_weight_2[nxt]
            if w1 > w2:
                dp_weight_3[i] = w1
                dp_indices_3[i] = dp_indices_3[i + 1]
            elif w2 > w1:
                dp_weight_3[i] = w2
                dp_indices_3[i] = insert_sorted(dp_indices_2[nxt], orig_idx)
            else:
                idx1 = dp_indices_3[i + 1]
                idx2 = insert_sorted(dp_indices_2[nxt], orig_idx)
                if idx1 < idx2:
                    dp_weight_3[i] = w1
                    dp_indices_3[i] = idx1
                else:
                    dp_weight_3[i] = w2
                    dp_indices_3[i] = idx2
            w1 = dp_weight_4[i + 1]
            w2 = w_val + dp_weight_3[nxt]
            if w1 > w2:
                dp_weight_4[i] = w1
                dp_indices_4[i] = dp_indices_4[i + 1]
            elif w2 > w1:
                dp_weight_4[i] = w2
                dp_indices_4[i] = insert_sorted(dp_indices_3[nxt], orig_idx)
            else:
                idx1 = dp_indices_4[i + 1]
                idx2 = insert_sorted(dp_indices_3[nxt], orig_idx)
                if idx1 < idx2:
                    dp_weight_4[i] = w1
                    dp_indices_4[i] = idx1
                else:
                    dp_weight_4[i] = w2
                    dp_indices_4[i] = idx2
        return dp_indices_4[0]
