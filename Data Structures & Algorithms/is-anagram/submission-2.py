from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # This is O(1) space because there can be at most 26 characters as keys
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for char in s:
            s_dict[char] += 1
        
        for char in t:
            t_dict[char] += 1
        
        for char in s:
            if s_dict[char] != t_dict[char]:
                return False
        
        for char in t:
            if t_dict[char] != s_dict[char]:
                return False
        
        return True