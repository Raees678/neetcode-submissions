class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def is_ascii(c):
            return "a" <= c <= "z" or "A" <= c <= "Z" or "0" <= c <= "9"
        

        hi = len(s) - 1
        lo = 0

        while lo < hi:
            low_c = s[lo]
            hi_c = s[hi]

            if not is_ascii(low_c):
                print("lo not ascii")
                lo += 1
                continue
            
            if not is_ascii(hi_c):
                print("high not ascii")
                hi -= 1
                continue
                    
            if low_c.lower() == hi_c.lower():
                lo += 1
                hi -= 1
                continue
            else:
                return False
        
        return True