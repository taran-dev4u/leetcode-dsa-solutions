class Solution:

    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if n <= 1:
            return
        k %= n
        if k == 0:
            return

        def reverse(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = (nums[end], nums[start])
                start += 1
                end -= 1
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
