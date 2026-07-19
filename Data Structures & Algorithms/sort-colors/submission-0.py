class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums) - 1
        curr = 0

        while curr <= high: 
            if nums[curr] == 0:
                temp = nums[low]
                nums[low] = nums[curr]
                nums[curr] = temp
                curr += 1
                low += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                temp = nums[high]
                nums[high] = nums[curr]
                nums[curr] = temp
                high -= 1
        