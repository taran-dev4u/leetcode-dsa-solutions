from typing import List

class Solution:

    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        sr, sc = (-1, -1)
        litter_idx = [[-1] * n for _ in range(m)]
        k = 0
        for r in range(m):
            for c in range(n):
                char = classroom[r][c]
                if char == 'S':
                    sr, sc = (r, c)
                elif char == 'L':
                    litter_idx[r][c] = k
                    k += 1
        if k == 0:
            return 0
        target_mask = (1 << k) - 1
        size = m << k + 5
        max_energy = [-1] * size
        init_idx = sr << k + 5 | sc << k
        max_energy[init_idx] = energy
        current_level = [(sr, sc, 0, energy)]
        steps = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while current_level:
            next_level = {}
            for r, c, mask, e in current_level:
                if mask == target_mask:
                    return steps
                if e <= 0:
                    continue
                for dr, dc in dirs:
                    nr, nc = (r + dr, c + dc)
                    if 0 <= nr < m and 0 <= nc < n:
                        char = classroom[nr][nc]
                        if char == 'X':
                            continue
                        ne = energy if char == 'R' else e - 1
                        nm = mask | 1 << litter_idx[nr][nc] if char == 'L' else mask
                        if nm == target_mask:
                            return steps + 1
                        n_idx = nr << k + 5 | nc << k | nm
                        if ne > max_energy[n_idx]:
                            if ne > next_level.get(n_idx, -1):
                                next_level[n_idx] = ne
            if not next_level:
                break
            current_level = []
            steps += 1
            for idx, ne in next_level.items():
                max_energy[idx] = ne
                nm = idx & target_mask
                nc = idx >> k & 31
                nr = idx >> k + 5
                current_level.append((nr, nc, nm, ne))
        return -1
