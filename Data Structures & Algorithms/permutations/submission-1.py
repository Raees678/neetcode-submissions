class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def perm(used_indices):
            if len(path) == len(nums):
                res.append(path.copy())
            
            for j in range(0, len(nums)):
                if j in used_indices:
                    continue
                path.append(nums[j])
                used_indices.add(j)
                perm(used_indices)
                used_indices.remove(j)
                path.pop()
            
        perm(set())
        return res

