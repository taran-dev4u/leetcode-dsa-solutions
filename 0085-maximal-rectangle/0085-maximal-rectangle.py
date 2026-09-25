class Solution:

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        cols = len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0
        for row in matrix:
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(cols + 1):
                h_i = heights[i]
                while len(stack) > 1 and h_i < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    area = h * w
                    if area > max_area:
                        max_area = area
                stack.append(i)
        return max_area
