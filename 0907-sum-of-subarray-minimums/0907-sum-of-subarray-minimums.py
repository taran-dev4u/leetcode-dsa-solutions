class Solution:

    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(arr)
        left = [0] * n
        right = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)
        ans = 0
        for i in range(n):
            ans = (ans + arr[i] * left[i] * right[i]) % MOD
        return ans
