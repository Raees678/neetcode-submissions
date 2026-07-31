class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        def helper(i):
            if i >= len(nums):
                return

            new_subsets = []
            for s in subsets:
                new_s = s.copy()
                new_s.append(nums[i])
                new_subsets.append(new_s)
            subsets.extend(new_subsets)

            helper(i+1)
        
        helper(0)

        return subsets
