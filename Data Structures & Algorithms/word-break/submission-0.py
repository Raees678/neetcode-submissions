from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        @cache
        def rec(i):
            if i == len(s):
                return True
            
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in words:
                    if rec(j):
                        return True
            return False
        

        return rec(0)