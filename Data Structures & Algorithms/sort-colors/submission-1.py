class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums) - 1
        curr = 0
        # loop invariants
        # 1. everything before low is 0
        # 2. everything b/w low and before curr is 1
        # 3. everything b/w curr and high is ?
        # 4. everything after high is 2

        while curr <= high: 
            # when doing this swap either low == curr so both must increment (case 1 invariant)
            # or curr is after low and you found ? to be a 0
            # and you are swapping it with a previously seen 1 (case 2 invariant)
            # when you do you must increment curr to mantain case 2.
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
        