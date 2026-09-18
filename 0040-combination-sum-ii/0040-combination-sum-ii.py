from collections import Counter

class Solution:

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        counts = Counter((c for c in candidates if c <= target))
        unique_candidates = sorted(counts.keys())
        n = len(unique_candidates)
        suffix_sums = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            val = unique_candidates[i]
            suffix_sums[i] = suffix_sums[i + 1] + val * counts[val]
        results = []
        current_path = []

        def backtrack(idx: int, rem: int) -> None:
            if rem == 0:
                results.append(list(current_path))
                return
            if idx == n or rem > suffix_sums[idx]:
                return
            val = unique_candidates[idx]
            if val > rem:
                return
            max_count = min(counts[val], rem // val)
            backtrack(idx + 1, rem)
            for k in range(1, max_count + 1):
                current_path.append(val)
                backtrack(idx + 1, rem - k * val)
            for _ in range(max_count):
                current_path.pop()
        backtrack(0, target)
        return results
