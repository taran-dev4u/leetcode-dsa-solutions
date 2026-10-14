class Solution:

    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ''
        c9, r = divmod(sum, 9)
        c0 = num - c9 - (1 if r > 0 else 0)
        if r > 0:
            return '9' * c9 + str(r) + '0' * c0
        else:
            return '9' * c9 + '0' * c0
