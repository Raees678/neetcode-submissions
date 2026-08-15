from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins, key=lambda x: -x)

        @cache
        def backtrack(i, target):
            if i >= len(coins):
                if target == 0:
                    return 0
                else:
                    return float("inf")

            # try to use 0 ... n from coins[i]
            num = 0
            remainder = target - num * coins[i]
            res = float("inf")
            while remainder >= 0:
                curr = num + backtrack(i+1, remainder)
                res = min(curr, res)
                num += 1
                remainder = target - num * coins[i]
            
            print(i, target, res)
            return res
        
        res = backtrack(0, amount)
        return -1 if res == float("inf") else res
            

            
