class Solution:

    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        if k == 0:
            return sum(((a - b) ** 2 for a, b in zip(nums1, nums2)))
        freq = [0] * 100001
        max_d = 0
        for a, b in zip(nums1, nums2):
            d = abs(a - b)
            freq[d] += 1
            if d > max_d:
                max_d = d
        for v in range(max_d, 0, -1):
            if freq[v] == 0:
                continue
            if k >= freq[v]:
                k -= freq[v]
                freq[v - 1] += freq[v]
                freq[v] = 0
            else:
                freq[v - 1] += k
                freq[v] -= k
                break
        return sum((v * v * freq[v] for v in range(1, max_d + 1)))
