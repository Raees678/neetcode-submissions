class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        end = len(nums) - 1
        count = 0

        while curr <= end:
            if nums[curr] == val:
                nums[curr] = nums[end]
                nums[end] = val
                end -= 1
                count += 1
            else:
                curr += 1
        
        return len(nums) - count

        

        

