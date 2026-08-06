class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def comb(i):
            res.append(path.copy())

            for idx in range(i, len(nums)):
                path.append(nums[idx])
                comb(idx + 1)
                path.pop()
        
        comb(0)
        return res