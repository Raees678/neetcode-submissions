class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        temp = None
        hi = len(s) - 1
        lo = 0
        while lo < hi:
            temp = s[lo]
            s[lo] = s[hi]
            s[hi] = temp
        
            lo += 1
            hi -= 1
        