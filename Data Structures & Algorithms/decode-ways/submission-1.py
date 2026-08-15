from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0

        def valid(i, j):
            if 0 <= i < len(s) and 0 <= j < len(s):
                if i == j:
                    return 1 <= int(s[i]) <= 26
                else:
                    return s[i] != "0" and 1 <= int(s[i:j+1]) <= 26
            else:
                return False

        @cache
        def backtrack(i):
            nonlocal res
            if i > len(s):
                return 0
            if i == len(s):
                return 1
            
            res = 0
            if valid(i, i):
                res = backtrack(i+1)
            
            if valid(i, i+1):
                res += backtrack(i+2)
            return res
        
        backtrack(0)
        return res
        