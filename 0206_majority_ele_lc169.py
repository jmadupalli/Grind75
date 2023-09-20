from typing import List

# https://leetcode.com/problems/majority-element/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # can be easily solved using a hashmap
        # instead using Moore's voting algorithm (count > n/2, exact case)

        curr = count = 0

        # select a candidate to be majority
        # increment/decrement count accordingly
        # when count is 0, change the candidate element
        for i in range(len(nums)):
            if nums[curr] == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                curr = i
                count = 1
        return nums[curr]

        # at the end of the loop, candidate will be majority

        # time complexity: O(n)
        # space complexity: O(1)
