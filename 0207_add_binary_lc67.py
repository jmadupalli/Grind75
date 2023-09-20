# https://leetcode.com/problems/add-binary

class Solution:
    # param 1: binary string
    # param 2: binary string
    # return: binary string of the sum
    def addBinary(self, a: str, b: str) -> str:

        # i tend to avoid one liners in general
        # but this deserves it, convert both strings
        # to integer, add, and convert back to binary
        return bin(int(a, 2) + int(b, 2))[2:]
