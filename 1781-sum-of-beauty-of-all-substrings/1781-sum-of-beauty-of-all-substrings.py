class Solution:

    def beautySum(self, s: str) -> int:
        total_beauty = 0
        n = len(s)
        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                char_idx = ord(s[j]) - ord('a')
                freq[char_idx] += 1
                max_freq = 0
                min_freq = float('inf')
                for f in freq:
                    if f > 0:
                        if f > max_freq:
                            max_freq = f
                        if f < min_freq:
                            min_freq = f
                total_beauty += max_freq - min_freq
        return total_beauty
