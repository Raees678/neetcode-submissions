class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in s:
                return [s[complement], idx]
            
            s[num] = idx
        
        raise Error("Shouldn't get here")
            
        