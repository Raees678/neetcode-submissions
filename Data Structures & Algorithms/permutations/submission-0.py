class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def perm(buffer, used_indices):
            if len(buffer) == len(nums):
                res.append(buffer.copy())
            
            for j in range(0, len(nums)):
                if j in used_indices:
                    continue
                buffer.append(nums[j])
                used_indices.add(j)
                perm(buffer, used_indices)
                used_indices.remove(j)
                buffer.pop()
            
        perm([], set())
        return res

