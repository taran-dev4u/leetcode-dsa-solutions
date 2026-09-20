class Solution:

    def addOperators(self, num: str, target: int) -> list[str]:
        n = len(num)
        ans = []
        path = []

        def dfs(idx: int, prev: int, curr: int):
            if idx == n:
                if curr == target:
                    ans.append(''.join(path))
                return
            val = 0
            for i in range(idx, n):
                if i > idx and num[idx] == '0':
                    break
                val = val * 10 + (ord(num[i]) - 48)
                s = num[idx:i + 1]
                if idx == 0:
                    path.append(s)
                    dfs(i + 1, val, val)
                    path.pop()
                else:
                    path.append('+')
                    path.append(s)
                    dfs(i + 1, val, curr + val)
                    path.pop()
                    path.pop()
                    path.append('-')
                    path.append(s)
                    dfs(i + 1, -val, curr - val)
                    path.pop()
                    path.pop()
                    path.append('*')
                    path.append(s)
                    dfs(i + 1, prev * val, curr - prev + prev * val)
                    path.pop()
                    path.pop()
        dfs(0, 0, 0)
        return ans
