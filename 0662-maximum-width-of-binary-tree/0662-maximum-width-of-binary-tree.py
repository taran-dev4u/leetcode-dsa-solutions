class Solution:

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_width = 0
        queue = [(root, 0)]
        while queue:
            max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
            next_queue = []
            for node, index in queue:
                if node.left:
                    next_queue.append((node.left, 2 * index))
                if node.right:
                    next_queue.append((node.right, 2 * index + 1))
            queue = next_queue
        return max_width
