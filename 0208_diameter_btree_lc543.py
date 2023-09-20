# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is the max of (lh + rh) for each node in btree
        diameter = [0]

        def height(node):
            if not node:
                return 0

            # recursively find the height of each node

            left = height(node.left)
            right = height(node.right)

            # maintain a global diameter, and keep changing it accordingly

            diameter[0] = max(diameter[0], left + right)

            return 1 + max(left, right)

        # invoke the recursive function from root
        height(root)

        # return the diameter
        return diameter[0]

        # PS: python has nuances with global variable assignments
        # in local scopes, just got to know :)

        # time complexity: O(n)
