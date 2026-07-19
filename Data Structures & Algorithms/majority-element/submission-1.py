class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # When dealing with counting more than half of an array 
        # you can use boyer moore voting

        count = 0
        res = None

        for num in nums:
            if num == res:
                count += 1
            else:
                count -= 1
            
            if count < 0:
                res = num
                count = 1
        
        return res
        