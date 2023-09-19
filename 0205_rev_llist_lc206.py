from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # param: head of the linked list
    # return: head of the reversed list
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # game of references :)
        prev, curr = None, head

        # we traverse the list till the end
        # and switch next references of each node
        # to point to the previous node until we reach the end
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # trace out the statements in the loop to get a clear idea

        # we return the last node of the original list
        # now it is the head of the reversed list
        return prev
