# https://leetcode.com/problems/valid-palindrome/
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert to lowercase
        s = s.lower()
        # remove all non-alphanumber characters
        s = re.sub('[^a-z0-9]', '', s)
        # use two pointers
        l, r = 0, len(s)-1
        while l<=r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

        # an alternate strategy would be to compare it with reverse
        # if s != s[::-1]: return False
    # time complexity: O(n)