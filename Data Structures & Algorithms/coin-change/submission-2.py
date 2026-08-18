from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def rec(i, amount):
            if amount == 0:
                return 0
            if i >= len(coins) or amount < 0:
                return float("inf")
            # Either take a coin and possibly take more of its values
            l = 1 + rec(i, amount - coins[i])
            # Or dont take the coin
            r = rec(i+1, amount)
            return min(l, r)

        res = rec(0, amount)
        if res == float("inf"):
            return -1
        return res