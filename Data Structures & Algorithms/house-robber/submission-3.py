from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def rec(i):
            # returns the max amt obtained robbing house i and then moving on or not robbing the house and moving on            
            amt = nums[i]
            res = nums[i]
            
            for j in range(i+2, len(nums)):
                res = max(res, amt + rec(j))
            
            for j in range(i+1, len(nums)):
                res = max(res, rec(j))

            return res

        return rec(0)
