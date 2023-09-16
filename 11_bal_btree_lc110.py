# https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # a nested recursive function
        def dfs(root):
            # base case for recursion
            if not root:
                return [True, 0]
            # check if its balanced recursively
            left, right = dfs(root.left), dfs(root.right)
            # is the tree balanced so far?
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            # return the current computation
            return [balanced, 1+max(left[1], right[1])]

        # return the boolean value
        return dfs(root)[0]
