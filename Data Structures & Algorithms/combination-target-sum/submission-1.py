class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def comb(i, s):
            if s == target:
                res.append(path.copy())
            
            if s > target:
                return

            for idx in range(i, len(nums)):
                path.append(nums[idx])
                comb(idx, s + nums[idx])
                path.pop()

        comb(0, 0)
        return res