from collections import Counter

class Solution:

    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        m = n // 2
        count_s = Counter(s)
        odd_chars = [char for char, count in count_s.items() if count % 2 != 0]
        if len(odd_chars) > (1 if n % 2 != 0 else 0):
            return ''
        mid_char = odd_chars[0] if odd_chars else ''
        H = Counter()
        for char, count in count_s.items():
            H[char] = count // 2
        candidates = []
        curr_H = Counter(H)
        for d in range(m):
            best_c = None
            for code in range(ord(target[d]) + 1, ord('z') + 1):
                char = chr(code)
                if curr_H[char] > 0:
                    best_c = char
                    break
            if best_c is not None:
                rem_H = Counter(curr_H)
                rem_H[best_c] -= 1
                suffix_chars = []
                for code in range(ord('a'), ord('z') + 1):
                    char = chr(code)
                    suffix_chars.append(char * rem_H[char])
                suffix_str = ''.join(suffix_chars)
                L = target[:d] + best_c + suffix_str
                P = L + mid_char + L[::-1]
                candidates.append(P)
            if curr_H[target[d]] > 0:
                curr_H[target[d]] -= 1
            else:
                break
        else:
            if n % 2 != 0:
                if mid_char > target[m]:
                    L = target[:m]
                    P = L + mid_char + L[::-1]
                    candidates.append(P)
                if mid_char == target[m]:
                    L = target[:m]
                    P = L + mid_char + L[::-1]
                    if P > target:
                        candidates.append(P)
            else:
                L = target[:m]
                P = L + L[::-1]
                if P > target:
                    candidates.append(P)
        return min(candidates) if candidates else ''
