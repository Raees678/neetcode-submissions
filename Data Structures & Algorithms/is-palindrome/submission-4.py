class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        def isAlphanumeric(c):
            return (ord("a") <= ord(c) <= ord("z")) or \
                (ord("A") <= ord(c) <= ord("Z")) or \
                (ord("0") <= ord(c) <= ord("9"))

        while i < j:
            if not isAlphanumeric(s[i]):
                i += 1
                continue
            if not isAlphanumeric(s[j]):
                j -= 1
                continue
            
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        
        return True