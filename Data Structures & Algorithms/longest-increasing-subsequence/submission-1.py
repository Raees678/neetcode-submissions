from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def rec(i):
            if i == len(nums) - 1:
                return 1, nums[i]
            
            curr = nums[i]
            res = 1
            for j in range(i+1, len(nums)):
                next_len, next_val = rec(j)
                if curr < next_val:
                    res = max(res, 1 + next_len)
            
            return res, curr
        
        res = 0
        for i in range(len(nums)):
            curr, _ = rec(i)
            res = max(res, curr)

        return res
            

            
            