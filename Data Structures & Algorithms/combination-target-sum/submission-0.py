class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def comb(i, buffer, buffer_sum):
            if buffer_sum == target:
                res.append(buffer.copy())
                return

            if buffer_sum > target:
                return
            
            for i in range(i, len(nums)):
                buffer.append(nums[i])
                comb(i, buffer, buffer_sum + nums[i])
                buffer.pop()
            
            return

        comb(0, [], 0)
        return res