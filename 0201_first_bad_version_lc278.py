# https://leetcode.com/problems/first-bad-version

class Solution:
    # param: n - the number of versions
    def firstBadVersion(self, n: int) -> int:

        # we have to find the first bad version
        # with minimum calls to the isBadVersion() method
        # we can do this with binary search!
        l, h = 1, n

        curr_min = n

        while l <= h:
            mid = (l+h) // 2

            # our target here is a bad version, we know if one version is bad
            # the versions post that are also bad, so we decrement high bound
            # if we found a bad version to in the hopes of finding the first one
            if isBadVersion(mid):
                # track the most minimum version, i.e our result
                curr_min = min(curr_min, mid)
                h = mid - 1
            else:
                # if the middle is not bad, i.e we have to look in the further versions
                # so we increment our low bound
                l = mid + 1
        return curr_min

        # time complexity: O(log n)
