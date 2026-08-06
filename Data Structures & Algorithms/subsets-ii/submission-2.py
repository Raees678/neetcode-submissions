class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        path = []

        def comb(i):
            res.append(path.copy())

            for j in range(i, len(nums)):
                if j == i or nums[j] != nums[j-1]:
                    path.append(nums[j])
                    comb(j+1)
                    path.pop()

        comb(0)
        return res

