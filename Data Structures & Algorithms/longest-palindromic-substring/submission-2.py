from functools import cache
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome_len(i, j):
            while 0 <= i <= len(s) and 0 <= j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            
            i += 1
            j -= 1
            return j - i + 1, i, j
        
        max_len = 0
        start, end = -1, -1
        for i in range(len(s)):
            l, p, q = palindrome_len(i, i)
            if l > max_len:
                max_len = l
                start = p
                end = q
        
        for i in range(len(s) - 1):
            l, p, q = palindrome_len(i, i+1)
            if l > max_len:
                max_len = l
                start = p
                end = q
        
        return s[start:end+1]
        