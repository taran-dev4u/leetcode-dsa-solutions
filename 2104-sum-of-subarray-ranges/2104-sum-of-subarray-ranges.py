class Solution:

    def subArrayRanges(self, nums: list[int]) -> int:
        n = len(nums)

        def get_sum(op):
            ans = 0
            stack = []
            for i in range(n + 1):
                while stack and (i == n or op(nums[stack[-1]], nums[i])):
                    mid = stack.pop()
                    left = mid - stack[-1] if stack else mid + 1
                    right = i - mid
                    ans += nums[mid] * left * right
                stack.append(i)
            return ans
        return get_sum(lambda a, b: a < b) - get_sum(lambda a, b: a > b)
