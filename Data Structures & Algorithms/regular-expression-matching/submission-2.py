from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def rec(i, j):
            # if i < len(s):
            #     print("s:", s[i:])
            # else:
            #     print("s done")
            
            # if j < len(p):
            #     print("p:", p[j:])
            # else:
            #     print("p done")

            if i == len(s) and j == len(p):
                return True
            
            matched = False
            if i < len(s) and j < len(p) and (s[i] == p[j] or "." == p[j]):
                matched = True
            
            
            if matched and j + 1 < len(p) and p[j+1] == "*":
                return rec(i + 1, j) or rec(i + 1, j + 2) or rec(i, j + 2)
            elif matched:
                return rec(i+1, j+1)
            
            if not matched and j + 1 < len(p) and p[j+1] == "*":
                return rec(i, j + 2)
            
            return False
        
        return rec(0, 0)

