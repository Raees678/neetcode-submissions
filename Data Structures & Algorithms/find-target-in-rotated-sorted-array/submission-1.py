class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def pred(idx):
            if target > nums[-1]:
                return nums[idx] >= target or nums[idx] <= nums[-1]
            else:
                return nums[idx] >= target and nums[idx] <= nums[-1]

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if pred(mid):
                r = mid - 1
            else:
                l = mid + 1


        if l < len(nums) and nums[l] == target:
            return l
        return -1