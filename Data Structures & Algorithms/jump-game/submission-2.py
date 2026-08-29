from functools import cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @cache
        def jump(i):
            if i >= len(nums):
                return False

            if i == len(nums) - 1:
                return True
            
            for j in reversed(range(1, nums[i] + 1)):
                if jump(i + j):
                    return True
            
            return False
        
        return jump(0)


            

