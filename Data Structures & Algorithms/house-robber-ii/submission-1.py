from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        @cache
        def rec(i, end):
            if i >= end:
                return 0
            amt = nums[i]
            res = max(amt + rec(i+2, end), rec(i+1, end))
            
            return res
        
        return max(rec(0, len(nums)-1), rec(1, len(nums)))
        
        

                

            