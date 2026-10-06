class Solution:

    def countNodes(self, root: TreeNode | None) -> int:

        def get_depth(node: TreeNode | None) -> int:
            d = 0
            while node:
                d += 1
                node = node.left
            return d
        count = 0
        curr = root
        while curr:
            ld = get_depth(curr.left)
            rd = get_depth(curr.right)
            if ld == rd:
                count += 1 << ld
                curr = curr.right
            else:
                count += 1 << rd
                curr = curr.left
        return count
