from collections import Counter

class Solution:

    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        parts = [char * count for char, count in counts.most_common()]
        return ''.join(parts)
