from collections import defaultdict

class Solution:

    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        col_table = defaultdict(list)
        stack = [(root, 0, 0)]
        min_col = max_col = 0
        while stack:
            node, r, c = stack.pop()
            col_table[c].append((r, node.val))
            if c < min_col:
                min_col = c
            elif c > max_col:
                max_col = c
            if node.right:
                stack.append((node.right, r + 1, c + 1))
            if node.left:
                stack.append((node.left, r + 1, c - 1))
        res = []
        for c in range(min_col, max_col + 1):
            col_table[c].sort()
            res.append([val for _, val in col_table[c]])
        return res
