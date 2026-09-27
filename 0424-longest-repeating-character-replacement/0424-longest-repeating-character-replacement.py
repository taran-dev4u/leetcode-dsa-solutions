class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        max_freq = 0
        left = 0
        ord_A = ord('A')
        for right in range(len(s)):
            idx = ord(s[right]) - ord_A
            count[idx] += 1
            if count[idx] > max_freq:
                max_freq = count[idx]
            if right - left + 1 - max_freq > k:
                count[ord(s[left]) - ord_A] -= 1
                left += 1
        return len(s) - left
