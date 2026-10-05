from collections import deque
from typing import List

class Solution:

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        parent_map = {}

        def build_parent_map(node, parent):
            if not node:
                return
            parent_map[node] = parent
            build_parent_map(node.left, node)
            build_parent_map(node.right, node)
        build_parent_map(root, None)
        queue = deque([(target, 0)])
        visited = {target}
        result = []
        while queue:
            node, dist = queue.popleft()
            if dist == k:
                result.append(node.val)
            elif dist < k:
                for neighbor in (node.left, node.right, parent_map.get(node)):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, dist + 1))
        return result
