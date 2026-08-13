from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def rec(i):
            if i >= len(nums):
                return 0
            # returns the max amt obtained robbing house i and then moving on or not robbing the house and moving on            
            amt = nums[i]
            res = 0
            
            res = max(res, amt + rec(i+2))
            res = max(res, rec(i+1))

            return res

        return rec(0)
