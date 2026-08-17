from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def rec(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            # if t1[i] and t2[j] are equal they are either part of the lcs
            # or not and check the remaining i+1, j+1
            # if they are unequal then check i+1, j or i, j+1 
            # this way we check all combos of i and j

            r1 = r2 = r3 = r4 = 0
            if text1[i] == text2[j]:
                r1 = 1 + rec(i+1, j+1)
                r2 = rec(i+1, j+1)
            else:
                r3 = rec(i+1, j)
                r4 = rec(i, j+1)
            
            return max(r1, r2, r3, r4)

        
        return rec(0,0)
