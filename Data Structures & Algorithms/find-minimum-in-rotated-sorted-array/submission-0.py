class Solution:
    def findMin(self, nums: List[int]) -> int:
        def pred(n):
            return n <= nums[-1]
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if pred(nums[mid]):
                r = mid - 1
            else:
                l = mid + 1
        
        return nums[l]

        