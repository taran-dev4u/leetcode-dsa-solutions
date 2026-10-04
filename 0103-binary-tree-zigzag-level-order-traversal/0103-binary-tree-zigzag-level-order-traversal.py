from collections import deque

class Solution:

    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        left_to_right = True
        while queue:
            level_size = len(queue)
            level_nodes = [0] * level_size
            for i in range(level_size):
                node = queue.popleft()
                index = i if left_to_right else level_size - 1 - i
                level_nodes[index] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)
            left_to_right = not left_to_right
        return result
