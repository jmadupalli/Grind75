from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # using 2 pointers 
        l, r = 0, 1
        mP = 0

        while r < len(prices):
            # check if it is profitable
            if prices[r] > prices[l]:
                # if so compare it with current max
                mP = max(mP, prices[r] - prices[l])
            else:
                # when left is smaller than right
                # it is a new case for profitability, we should consider buying on this new low
                l = r
            # keep shifting right pointer
            r += 1
        return mP

    # time compleity: O(n)