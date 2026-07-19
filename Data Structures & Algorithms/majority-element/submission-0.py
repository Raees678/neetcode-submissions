from random import randint
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def count(el):
            res = 0
            for num in nums:
                if num == el:
                    res += 1
            return res
        
        while True:
            idx = randint(0, len(nums) - 1)
            el = nums[idx]
            if count(el) > len(nums) / 2:
                return el


