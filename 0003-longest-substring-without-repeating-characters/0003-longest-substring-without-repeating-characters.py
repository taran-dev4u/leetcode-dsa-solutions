class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        max_len = 0
        start = 0
        for end, char in enumerate(s):
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            last_seen[char] = end
            current_len = end - start + 1
            if current_len > max_len:
                max_len = current_len
        return max_len
