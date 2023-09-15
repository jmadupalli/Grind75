# https://leetcode.com/problems/invert-binary-tree/
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # handle an empty binary tree
        if not root:
            return root
        # surprise! surprise! we're using a queue
        q = deque()
        q.appendleft(root)
        
        while len(q) > 0:
            # get element from queue
            curr = q.pop()
            # swap/invert as requested
            curr.left, curr.right = curr.right, curr.left

            # insert nodes if they exist again to process further
            if curr.left:
                q.appendleft(curr.left)
            if curr.right:
                q.appendleft(curr.right)
        return root

        # this is basically level order traversal (bfs) 
        # we can also use other traversals (dfs), using stack/recursion
        # time complexity: O(n)
        # space: O(n)

        # rec solution:

        # def invertTree(self, root):
        #     if not root:
        #         return root
        #     root.left, root.right = root.right, root.left
        #     self.invertTree(root.left)
        #     self.invertTree(root.right)
        #     return root