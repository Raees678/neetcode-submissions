from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        @cache
        def rec(i, j):
            if j < i:
                return 0
            # choose to preserve a single idx k between i and j
            # making this call give nums[k-1] * nums[k] * j+1 coins
            # and then get subsequent vals from rec(i, k-1), rec(k+1, j)
            res = 0
            for k in range(i, j+1):
                coins = nums[i-1] * nums[k] * nums[j+1]
                coins += rec(i, k-1)
                coins += rec(k+1,j)
                res = max(res, coins)
            return res

                
        return rec(1, len(nums) - 2)