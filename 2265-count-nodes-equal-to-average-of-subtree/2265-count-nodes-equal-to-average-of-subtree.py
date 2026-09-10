class Solution:

    def averageOfSubtree(self, root: 'TreeNode') -> int:
        matching_nodes_count = 0

        def dfs(node) -> tuple:
            nonlocal matching_nodes_count
            if not node:
                return (0, 0)
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            curr_sum = left_sum + right_sum + node.val
            curr_count = left_count + right_count + 1
            if curr_sum // curr_count == node.val:
                matching_nodes_count += 1
            return (curr_sum, curr_count)
        dfs(root)
        return matching_nodes_count
