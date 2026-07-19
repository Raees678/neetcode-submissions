class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(low, high, skip_available):
            if low >= high:
                return True

            if s[low] == s[high]:
                return check(low + 1, high - 1, skip_available)
            else:
                if skip_available:
                    return check(low + 1, high, False) or check(low, high - 1, False)
                else: 
                    return False
            
        return check(0, len(s) - 1, True)

        