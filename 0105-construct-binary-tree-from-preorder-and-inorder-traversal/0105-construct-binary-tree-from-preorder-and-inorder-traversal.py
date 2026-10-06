class Solution:

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        preorder_iter = iter(preorder)

        def helper(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None
            val = next(preorder_iter)
            root = TreeNode(val)
            idx = inorder_index_map[val]
            root.left = helper(left, idx - 1)
            root.right = helper(idx + 1, right)
            return root
        return helper(0, len(inorder) - 1)
