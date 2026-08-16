from functools import cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def rec(i, t):
            if i == len(nums):
                return t == 0
            
            return rec(i+1, t - nums[i]) or rec(i + 1, t)
        
        s = sum(nums)
        if s % 2:
            return False
        return rec(0, s // 2)