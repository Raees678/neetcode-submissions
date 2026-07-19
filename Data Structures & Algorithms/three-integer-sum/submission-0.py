# [-4, -1, -1, 0, 1, 2]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        pivot = 0

        while pivot < len(nums):
            low = pivot + 1
            high = len(nums) - 1

            while low < high:
                s = nums[low] + nums[high]
                if s < -nums[pivot]:
                    old_low_num = nums[low]
                    low += 1
                    while low < len(nums) and nums[low] == old_low_num:
                        low += 1
                    continue
                if s > -nums[pivot]:
                    old_high_num = nums[high]
                    high -= 1
                    while high >= 0 and nums[high] == old_high_num:
                        high -= 1
                    continue
                if s == -nums[pivot]:
                    res.append([nums[pivot], nums[low], nums[high]])

                    old_low_num = nums[low]
                    low += 1
                    while low < len(nums) and nums[low] == old_low_num:
                        low += 1
                    old_high_num = nums[high]
                    high -= 1
                    while high >= 0 and nums[high] == old_high_num:
                        high -= 1
                    continue

            
            # advance pivot avoiding duplicates
            old_pivot_num = nums[pivot]
            pivot += 1
            while pivot < len(nums) and nums[pivot] == old_pivot_num:
                pivot += 1
        
        return res