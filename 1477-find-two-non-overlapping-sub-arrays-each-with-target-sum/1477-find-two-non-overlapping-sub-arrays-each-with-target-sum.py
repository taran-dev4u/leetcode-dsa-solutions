class Solution:

    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = 10 ** 9
        min_len = [INF] * n
        ans = INF
        current_sum = 0
        l = 0
        best_till_now = INF
        for r in range(n):
            current_sum += arr[r]
            while current_sum > target:
                current_sum -= arr[l]
                l += 1
            if current_sum == target:
                length = r - l + 1
                if l > 0 and min_len[l - 1] != INF:
                    ans = min(ans, length + min_len[l - 1])
                best_till_now = min(best_till_now, length)
            min_len[r] = best_till_now
        return ans if ans != INF else -1
