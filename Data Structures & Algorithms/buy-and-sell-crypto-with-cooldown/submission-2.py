from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def rec(i, bought):
            if i >= len(prices):
                return 0
            
            if bought:
                return max(prices[i] + rec(i+2, False), rec(i+1, True))
            else:
                return max(-prices[i] + rec(i+1, True), rec(i+1, False))

        return rec(0, False)
