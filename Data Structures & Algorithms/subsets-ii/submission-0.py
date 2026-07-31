class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        counter = Counter(nums)
        nums_count = [(num, count) for num, count in counter.items()]
        def helper(i):
            if i >= len(nums_count):
                return
            
            num, count = nums_count[i]
            print(num, count)

            new_subsets = []
            for s in subsets:
                val = []
                for c in range(count):
                    val.append(num)
                    s_copy = s.copy()
                    s_copy.extend(val.copy())
                    new_subsets.append(s_copy)
            
            subsets.extend(new_subsets)

            helper(i+1)
        
        helper(0)

        return subsets
        