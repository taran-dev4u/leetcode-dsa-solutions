class Solution:

    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(start: int, current_path: list[int]):
            result.append(list(current_path))
            for i in range(start, len(nums)):
                current_path.append(nums[i])
                backtrack(i + 1, current_path)
                current_path.pop()
        backtrack(0, [])
        return result
