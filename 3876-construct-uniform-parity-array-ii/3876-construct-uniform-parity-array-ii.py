class Solution:

    def uniformArray(self, nums1: list[int]) -> bool:
        o_min = float('inf')
        for x in nums1:
            if x % 2 != 0:
                if x < o_min:
                    o_min = x
        if o_min == float('inf'):
            return True
        for x in nums1:
            if x % 2 == 0:
                if x < o_min:
                    return False
        return True
