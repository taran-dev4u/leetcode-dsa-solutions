class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        open_needed = 0
        for char in s:
            if char == '(':
                open_count += 1
            elif open_count > 0:
                open_count -= 1
            else:
                open_needed += 1
        return open_count + open_needed
