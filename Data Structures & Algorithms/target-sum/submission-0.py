from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:        
        res = 0
        @cache
        def rec(i, sum):
            nonlocal res
            if i == len(nums) and sum == target:
                return 1
            
            if i >= len(nums):
                return 0

            
            res = 0
            res += rec(i+1, sum+nums[i])
            res += rec(i+1, sum-nums[i])
            return res

        rec(0, 0)
        return res