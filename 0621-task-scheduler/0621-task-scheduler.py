from collections import Counter

class Solution:

    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks)
        max_freq = max(counts.values())
        max_freq_count = sum((1 for count in counts.values() if count == max_freq))
        return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_count)
