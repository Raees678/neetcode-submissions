class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_allowed = 0
        i = 0

        while i <= max_allowed and i < len(nums):
            max_allowed = max(max_allowed, i + nums[i])
            i += 1
        
        return max_allowed >= len(nums) - 1
