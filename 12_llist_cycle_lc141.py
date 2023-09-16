# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using fast and slow pointers pattern
        slow = fast = head

        # concept is it to increment fast pointer twice
        # and slow only once, if there is a cycle
        # these pointers will be equal at some point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        # if the fast pointer reached the end, without
        # equating to slow at some point, there is no cycle
        return False
