from functools import cache

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        
        @cache
        def is_palindrome(s):
            if len(s) == 0:
                return False
            i = 0
            j = len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        
        def comb(i):
            if i == len(s):
                res.append(path.copy())
                return
            
            for idx in range(i, len(s)):
                substring = s[i:idx+1]
                if is_palindrome(substring):
                    path.append(substring)
                    comb(idx+1)
                    path.pop()
            
        comb(0)
            
        
        return res
