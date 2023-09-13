# LeetCode 1
from typing import List


class Solution:
    # @param1 nums: list of integers
    # @param2 target: the sum of 2 integers in the given list
    # return: a list of 2 integers (indexes of elements that sum to target)
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # maintain a lookup/dictionary to see if an element exists
        lookup = {}
        for i, n in enumerate(nums):
            # we have n, to find the number that sums to target:
            # we just see if target-n exists
            curr = target - n
            if curr in lookup:
                # if it does, we found the result
                return [lookup[curr], i]
            # if not, we update for lookup, assign the element as key and index as value
            lookup[n] = i

    # time complexity: O(n)
