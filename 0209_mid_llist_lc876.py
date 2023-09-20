from typing import Optional

# https://leetcode.com/problems/middle-of-the-linked-list/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # the fast and slow pointers technique, maintain two pointers
        slow = fast = head

        # slow pointer traverses at normal pace
        # fast goes 2x the pace
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # by the time fast reaches the end of list
        # slow will be at middle!

        return slow

        # time complexity: O(n)
