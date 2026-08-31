from functools import cache

class Solution:
    def jump(self, nums: List[int]) -> int:

        @cache
        def jump(i):
            if i >= len(nums):
                return float("inf")
            if i == len(nums) - 1:
                return 0
            
            res = float("inf")
            for d in range(1, nums[i]+1):
                res = min(res, 1 + jump(i + d))
            
            return res
        
        return jump(0)