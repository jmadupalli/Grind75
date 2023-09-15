from typing import Optional

# https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # @param1 list1: list1 to be merged
    # @param2 list2: list2 to be merged
    # return: head of the merged list
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a node to act as placeholder
        dummy = ListNode()
        temp = dummy

        # check if both lists are not empty
        # in this case, we have to find the smallest element of the both
        # add it to the new list, and update pointers accordingly
        while list1 and list2:
            if list1.val > list2.val:
                temp.next = list2
                list2 = list2.next
            else:
                temp.next = list1
                list1 = list1.next
            temp = temp.next

        # if list1 still has elements, add them all
        while list1:
            temp.next = list1
            list1 = list1.next
            temp = temp.next

        # if list2 still has elements, add them all
        # remember only one of the 2 lists have elements now
        while list2:
            temp.next = list2
            list2 = list2.next
            temp = temp.next

        # return the first/head element of merged list
        return dummy.next
