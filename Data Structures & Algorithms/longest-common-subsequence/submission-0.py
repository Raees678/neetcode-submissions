from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        positions = defaultdict(list)
        for idx, i in enumerate(text2):
            positions[i].append(idx)
        
        @cache
        def rec(i, j):
            if i == len(text1):
                return 0
            
            curr_l = text1[i]
            # find all pos of char in text2 >= j
            # either 1 + longest common sub(i+1,pos+1)
            # or dont include i and find longest common sub
            # between i+1 and j
            curr = res = rec(i+1, j)
            for k in positions[curr_l]:
                if k >= j:
                    curr = 1 + rec(i+1, k+1)
                    res = max(curr,res)
            print(curr, res)
            return res

        return rec(0, 0)

            

            
