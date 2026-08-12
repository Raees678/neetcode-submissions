from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def rec(i):
            # returns the max amt obtained robbing house i and then moving on
            if i >= len(nums):
                return 0
            
            amt = nums[i]
            max_next_amt = 0
            for j in range(i+2, len(nums)):
                next_amt = rec(j)
                max_next_amt = max(next_amt, max_next_amt)
            
            return amt + max_next_amt

        res = 0
        for i in range(len(nums)):
            res = max(res, rec(i))
        return res