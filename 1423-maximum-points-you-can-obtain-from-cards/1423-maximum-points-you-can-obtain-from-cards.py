class Solution:

    def maxScore(self, cardPoints: list[int], k: int) -> int:
        current_sum = sum(cardPoints[:k])
        max_sum = current_sum
        for i in range(1, k + 1):
            current_sum += cardPoints[-i] - cardPoints[k - i]
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum
