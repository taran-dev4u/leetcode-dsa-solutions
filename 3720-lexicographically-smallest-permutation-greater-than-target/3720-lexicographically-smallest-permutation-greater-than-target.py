class Solution:

    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        counts = [0] * 26
        for char in s:
            counts[ord(char) - 97] += 1
        counts_at_step = [list(counts)]
        L = 0
        for char in target:
            idx = ord(char) - 97
            if counts[idx] > 0:
                counts[idx] -= 1
                counts_at_step.append(list(counts))
                L += 1
            else:
                break
        for i in range(min(L, n - 1), -1, -1):
            target_idx = ord(target[i]) - 97
            for c_idx in range(target_idx + 1, 26):
                if counts_at_step[i][c_idx] > 0:
                    counts_at_step[i][c_idx] -= 1
                    suffix = []
                    for j in range(26):
                        if counts_at_step[i][j] > 0:
                            suffix.append(chr(j + 97) * counts_at_step[i][j])
                    return target[:i] + chr(c_idx + 97) + ''.join(suffix)
        return ''
