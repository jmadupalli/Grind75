# https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # just create a set, see if lengths match
        return len(nums) != len(set(nums))

        # space complexity: O(n)
        # time complexity: O(n) -> creating set from list
