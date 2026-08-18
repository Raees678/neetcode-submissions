from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def rec(i, amount):
            if i >= len(coins) or amount < 0:
                return 0
            if amount == 0:
                return 1
            
            res = 0
            res += rec(i, amount - coins[i])
            res += rec(i+1, amount)
            return res
        
        return rec(0, amount)
            

            
