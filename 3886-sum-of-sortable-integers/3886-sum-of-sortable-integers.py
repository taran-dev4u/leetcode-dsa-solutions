class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        divs = []
        d = 1
        while d * d <= n:
            if n % d == 0:
                divs.append(d)
                if d * d != n:
                    divs.append(n // d)
            d += 1
        divs.sort()

        is_sorted = True
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                is_sorted = False
                break
        if is_sorted:
            return sum(divs)

        ans = 0
        for k in divs:
            if k == 1:
                continue
            m = n // k
            possible = True
            last_val = -1
            for b in range(m):
                sub = nums[b * k : (b + 1) * k]
                drops = 0
                drop_idx = -1
                for j in range(k - 1):
                    if sub[j] > sub[j + 1]:
                        drops += 1
                        drop_idx = j
                        if drops > 1:
                            possible = False
                            break
                if not possible:
                    break
                if sub[-1] > sub[0]:
                    drops += 1
                    drop_idx = k - 1
                    if drops > 1:
                        possible = False
                        break
                rot_start = (drop_idx + 1) if drop_idx + 1 < k else 0
                if last_val != -1 and sub[rot_start] < last_val:
                    possible = False
                    break
                last_val = sub[drop_idx] if drops == 1 else sub[-1]
            if possible:
                ans += k
        return ans
