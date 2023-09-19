# https://leetcode.com/problems/longest-palindrome

class Solution:
    # param: the string to find the longest palindrome from
    def longestPalindrome(self, s: str) -> int:
        # hashmap to maintain character frequency
        counts = {}

        # initialize it
        for char in s:
            counts[char] = 1 + counts.get(char, 0)

        # the longest length is the sum all even counts of characters
        # plus odd count if exists (otherwise just sum of even counts)
        oddExists = False
        maxLen = 0

        # the below loop adds all even counts
        # we deduct 1 from odd counts to make them even
        for char in counts:
            if counts[char] % 2 == 0:
                maxLen += counts[char]
            else:
                oddExists = True
                maxLen += counts[char] - 1

        # and add one back if there was an odd count
        return maxLen + 1 if oddExists else maxLen

        # time complexity: O(n)
        # space complexity: O(n)
