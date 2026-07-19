class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        one_sol = all(num != 1 for num in nums)
        if one_sol:
            return 1
        
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = 1
        
        for num in nums:
            idx = num - 1
            while idx in range(len(nums)):
                num = nums[idx]
                nums[idx] = 0
                idx = num - 1
        
        for idx, num in enumerate(nums):
            if num > 0:
                return idx + 1
        
        return len(nums) + 1
        


                

        

                
            




