from typing import List

class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.tree = [None] * (4 * self.n)
        self.s = list(s)
        if self.n > 0:
            self._build(0, 0, self.n - 1)

    def _build(self, node: int, start: int, end: int):
        if start == end:
            self.tree[node] = {
                'left_char': self.s[start],
                'right_char': self.s[start],
                'left_len': 1,
                'right_len': 1,
                'max_len': 1,
                'length': 1
            }
            return
        mid = (start + end) // 2
        self._build(2 * node + 1, start, mid)
        self._build(2 * node + 2, mid + 1, end)
        self.tree[node] = self._merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def _merge(self, left_node, right_node):
        res = {}
        res['length'] = left_node['length'] + right_node['length']
        res['left_char'] = left_node['left_char']
        res['right_char'] = right_node['right_char']
        
        res['left_len'] = left_node['left_len']
        if left_node['left_len'] == left_node['length'] and left_node['left_char'] == right_node['left_char']:
            res['left_len'] += right_node['left_len']
            
        res['right_len'] = right_node['right_len']
        if right_node['right_len'] == right_node['length'] and right_node['right_char'] == left_node['right_char']:
            res['right_len'] += left_node['right_len']
            
        max_len = max(left_node['max_len'], right_node['max_len'])
        if left_node['right_char'] == right_node['left_char']:
            max_len = max(max_len, left_node['right_len'] + right_node['left_len'])
            
        res['max_len'] = max_len
        return res

    def update(self, idx: int, char: str):
        self._update(0, 0, self.n - 1, idx, char)

    def _update(self, node: int, start: int, end: int, idx: int, char: str):
        if start == end:
            self.s[idx] = char
            self.tree[node] = {
                'left_char': char,
                'right_char': char,
                'left_len': 1,
                'right_len': 1,
                'max_len': 1,
                'length': 1
            }
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self._update(2 * node + 1, start, mid, idx, char)
        else:
            self._update(2 * node + 2, mid + 1, end, idx, char)
        self.tree[node] = self._merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self) -> int:
        return self.tree[0]['max_len']

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        seg = SegmentTree(s)
        ans = []
        for char, idx in zip(queryCharacters, queryIndices):
            seg.update(idx, char)
            ans.append(seg.query())
        return ans
