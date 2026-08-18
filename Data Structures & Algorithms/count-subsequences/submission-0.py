from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        res = 0
        @cache
        def rec(i, j):
            nonlocal res
            if j == len(t):
                return 1
            
            if i >= len(s):
                return 0

            res = 0
            # match s[i] to t[j]
            if s[i] == t[j]:
                res += rec(i+1, j+1)
            
            # choose not to match s[i] to t[j]
            res += rec(i+1, j)
            return res
        
        return rec(0, 0)
            
        