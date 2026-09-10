class Solution:

    def averageOfSubtree(self, root: 'TreeNode') -> int:
        self.matching_nodes_count = 0

        def calculate_subtree_stats(node):
            if not node:
                return (0, 0)
            left_sum, left_count = calculate_subtree_stats(node.left)
            right_sum, right_count = calculate_subtree_stats(node.right)
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            if total_sum // total_count == node.val:
                self.matching_nodes_count += 1
            return (total_sum, total_count)
        calculate_subtree_stats(root)
        return self.matching_nodes_count
