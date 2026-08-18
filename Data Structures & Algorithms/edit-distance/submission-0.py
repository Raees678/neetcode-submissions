from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def rec(i, j):
            if i == len(word1) and j == len(word2):
                return 0
            
            if i < len(word1) and j == len(word2):
                # delete remaining chars from w1 to match
                return len(word1) - i
            
            if i == len(word1) and j < len(word2):
                # insert remaining chars into w1 to match
                return len(word2) - j
            
            # at this point both i and j point to chars
            d = ins = r = 0
            d = 1 + rec(i+1,j)
            ins = 1 + rec(i,j+1)
            if word1[i] == word2[j]:
                r = rec(i+1, j+1)
            else:
                r = 1 + rec(i+1,j+1)
            
            return min(d, ins, r)

        return rec(0, 0)
        