class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = [0] * 26
        t_count = [0] * 26

        for c in s:
            s_count[ord(c) - ord('a')] += 1
        for c in t:
            t_count[ord(c) - ord('a')] += 1
        
        for i in range(26):
            if s_count[i] != t_count[i]:
                return False
        
        return True
                
