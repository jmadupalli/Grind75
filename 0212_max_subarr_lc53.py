from typing import List

# https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maintain a current sum, and an assumed max
        curr_sum = 0
        max_sum = nums[0]
        for n in nums:
            # the strategy is to deny the subarray if the sum is -ve
            if curr_sum < 0:
                curr_sum = 0
            # add the current number
            curr_sum += n
            # compare the curr sum with max sum
            max_sum = max(max_sum, curr_sum)

        return max_sum

        # time complexity: O(n)
