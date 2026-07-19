class Solution:
    def maxArea(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        res = 0

        while low < high:
            curr = (high - low) * min(nums[low], nums[high])
            res = max(res, curr)

            if nums[low] <= nums[high]:
                low += 1
            elif nums[high] < nums[low]:
                high -= 1
        
        return res


        