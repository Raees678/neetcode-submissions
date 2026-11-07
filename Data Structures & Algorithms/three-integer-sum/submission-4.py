# [-1,0,1,2,-1,-4]
# [-4,-1,-1,0,1,2]
# 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                if k < len(nums) - 1 and nums[k] == nums[k+1]:
                    k -= 1
                    continue
                
                if nums[j] + nums[k] == -nums[i]:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1

        return res