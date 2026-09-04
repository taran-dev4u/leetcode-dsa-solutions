from typing import List

class Solution:

    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        if n == 1:
            return 0
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]
        dp = [[0] * n for _ in range(n)]
        max_left = [[0] * n for _ in range(n)]
        max_right = [[0] * n for _ in range(n)]
        for i in range(n):
            max_left[i][i] = stoneValue[i]
            max_right[i][i] = stoneValue[i]
        for i in range(n - 1, -1, -1):
            mid = i - 1
            pref_i = pref[i]
            max_left_i = max_left[i]
            dp_i = dp[i]
            max_right_i_plus_1 = max_right[i + 1] if i + 1 < n else None
            for j in range(i + 1, n):
                target = pref[j + 1] + pref_i
                while mid + 1 < j and pref[mid + 2] << 1 <= target:
                    mid += 1
                if mid < i:
                    val = max_right_i_plus_1[j]
                elif pref[mid + 1] << 1 == target:
                    val = max(max_left_i[mid], max_right[mid + 1][j])
                else:
                    val = max_left_i[mid]
                    if mid + 2 <= j:
                        r_val = max_right[mid + 2][j]
                        if r_val > val:
                            val = r_val
                dp_i[j] = val
                sum_ij = pref[j + 1] - pref_i
                val_ij = val + sum_ij
                prev_l = max_left_i[j - 1]
                max_left_i[j] = val_ij if val_ij > prev_l else prev_l
                prev_r = max_right_i_plus_1[j]
                max_right[i][j] = val_ij if val_ij > prev_r else prev_r
        return dp[0][n - 1]
