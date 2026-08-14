class Solution:
    def countSubstrings(self, s: str) -> int:
        def inbounds(i):
            return 0 <= i < len(s)

        def num_pals(i, j):
            res = 0
            while inbounds(i) and inbounds(j) and s[i] == s[j]:
                i -= 1
                j += 1
                res += 1
            
            return res
        
        res = 0
        for i in range(len(s)):
            res += num_pals(i, i)
        
        for i in range(len(s) - 1):
            res += num_pals(i, i + 1)
        
        return res

            

            
