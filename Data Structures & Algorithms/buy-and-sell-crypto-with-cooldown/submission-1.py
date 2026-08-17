from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def rec(i):
            if i >= len(prices):
                return 0
            res = curr = 0
            # choose to buy at i
            # sell at j
            # and then make other transactions at j+2
            for j in range(i, len(prices)):
                # single transaction from i
                curr = prices[j] - prices[i]
                # all future transactions from j+2
                fut = rec(j+2)
                res = max(res, curr + fut)
            
            # or choose to not buy at i
            # and make other transactions at i+1
            res = max(res, rec(i+1))
            return res
            

        return rec(0)
