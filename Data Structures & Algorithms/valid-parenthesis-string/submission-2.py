class Solution:
    def checkValidString(self, s: str) -> bool:
        open = stars = closed = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                open += 1
            elif s[i] == ")":
                closed += 1
            else:
                stars += 1
            
            if closed > open + stars:
                return False
        
        open = stars = closed = 0
        for i in reversed(range(len(s))):
            if s[i] == ")":
                open += 1
            elif s[i] == "(":
                closed += 1
            else:
                stars += 1
            
            if closed > open + stars:
                return False
        
        return True
        
