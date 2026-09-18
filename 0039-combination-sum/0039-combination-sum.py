from typing import List

class Solution:

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        results = []

        def backtrack(remain: int, start: int, path: list[int]):
            if remain == 0:
                results.append(list(path))
                return
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if candidate > remain:
                    break
                path.append(candidate)
                backtrack(remain - candidate, i, path)
                path.pop()
        backtrack(target, 0, [])
        return results
