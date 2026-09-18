class Solution:

    def maxNumOfSubstrings(self, s: str) -> list[str]:
        A = [ord(c) - 97 for c in s]
        L = [-1] * 26
        R = [-1] * 26
        for i, val in enumerate(A):
            if L[val] == -1:
                L[val] = i
            R[val] = i
        valid_intervals = []
        for char_idx in range(26):
            l = L[char_idx]
            if l == -1:
                continue
            r = R[char_idx]
            possible = True
            i = l
            while i <= r:
                c_idx = A[i]
                if L[c_idx] < l:
                    possible = False
                    break
                r = max(r, R[c_idx])
                i += 1
            if possible:
                valid_intervals.append((l, r))
        valid_intervals.sort(key=lambda x: (x[1], -x[0]))
        ans = []
        last_end = -1
        for l, r in valid_intervals:
            if l > last_end:
                ans.append(s[l:r + 1])
                last_end = r
        return ans
