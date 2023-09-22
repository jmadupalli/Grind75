# https://leetcode.com/problems/climbing-stairs/

# first dynamic programming problem of the list

class Solution:

    # found this to be a very tricky problem, thanks to NeetCode!
    def climbStairs(self, n: int) -> int:
        one = two = 1
        # the solution is basically returning the fibanocci number
        while n > 0:
            temp = two
            two = one + two
            one = temp
            n -= 1
        return one

        # but why? well, we're using the bottom up approach
        # come from the top, how many ways to reach from top? -> 1
        # how many ways to reach top from top-1? -> 1
        # how many ways to reach top from top-2? (1+1) + (2) -> 2
        # how many ways to reach top from top-3? (1+1+1) + (1+2) + (2+1) -> 3
        # see a pattern? it's fibanocci
