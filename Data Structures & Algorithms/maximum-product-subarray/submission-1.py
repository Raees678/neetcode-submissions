from functools import cache
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        @cache
        def rec(i):
            curr = nums[i]
            if i == 0:
                return curr, curr
            prev_max, prev_min = rec(i-1)
            curr_max = max(prev_max * curr, prev_min * curr, curr)
            curr_min = min(prev_max * curr, prev_min * curr, curr)
            return curr_max, curr_min

        res = float("-inf")
        for i in range(len(nums)):    
            curr, _ = rec(i)
            res = max(res, curr)
        
        return res
        
        