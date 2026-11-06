class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()

        for num in nums:
            s.add(num)
        
        res = 0
        for num in nums:
            if num - 1 in s:
                continue
            
            curr = num
            while curr in s:
                curr += 1
            
            res = max(curr - num, res)
        
        return res