from typing import Optional

# https://leetcode.com/problems/maximum-depth-of-binary-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # using recursive tree traversal and returning height
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # height is depth :)
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            return 1 + max(left, right)

        return height(root)

    # time complexity: O(n)
