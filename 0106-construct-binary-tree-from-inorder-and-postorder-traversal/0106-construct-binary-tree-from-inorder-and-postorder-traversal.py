class Solution:

    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        idx_map = {val: i for i, val in enumerate(inorder)}
        post_idx = len(postorder) - 1

        def helper(in_left: int, in_right: int) -> TreeNode | None:
            nonlocal post_idx
            if in_left > in_right:
                return None
            val = postorder[post_idx]
            post_idx -= 1
            root = TreeNode(val)
            root_idx = idx_map[val]
            root.right = helper(root_idx + 1, in_right)
            root.left = helper(in_left, root_idx - 1)
            return root
        return helper(0, len(inorder) - 1)
