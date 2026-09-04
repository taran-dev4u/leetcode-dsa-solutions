class Solution:

    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        s_l = s_r = q_l = q_r = 0
        for i in range(mid):
            if num[i] == '?':
                q_l += 1
            else:
                s_l += int(num[i])
        for i in range(mid, n):
            if num[i] == '?':
                q_r += 1
            else:
                s_r += int(num[i])
        return 2 * (s_l - s_r) != 9 * (q_r - q_l)
