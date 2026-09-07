from functools import cache

class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def rec(i, unclosed):
            if i == len(s) and unclosed == 0:
                return True
            
            if unclosed < 0 or i >= len(s):
                return False


            if s[i] == "(":
                return rec(i+1, unclosed+1)
            elif s[i] == ")":
                return rec(i+1, unclosed-1)
            else:
                return rec(i+1, unclosed) or rec(i+1, unclosed+1) or rec(i+1, unclosed-1)
            
        return rec(0, 0)
        