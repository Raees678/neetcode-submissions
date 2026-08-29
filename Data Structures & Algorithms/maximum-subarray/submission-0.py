class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = prev = nums[0]
        for i in range(1, len(nums)):
            curr = max(nums[i], nums[i] + prev)
            res = max(curr, res)
            prev = curr
        
        return res