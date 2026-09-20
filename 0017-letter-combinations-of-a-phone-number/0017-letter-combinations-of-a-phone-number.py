from typing import List
import itertools

class Solution:

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        pools = [mapping[digit] for digit in digits]
        return [''.join(combination) for combination in itertools.product(*pools)]
