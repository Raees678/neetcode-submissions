from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def rec(i, j):
            k = i + j
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            
            l = r = False
            if i < len(s1) and k < len(s3) and s1[i] == s3[k]:
                l = rec(i+1, j)

            if j < len(s2) and k < len(s3) and s2[j] == s3[k]:
                r = rec(i, j+1)
            
            return l or r
        
        return rec(0, 0)

            