from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def rec(n):
            if n < 0:
                return 0

            if n == 0:
                return 1
            
            onestep = rec(n-1)
            twosteps = rec(n-2)
            return onestep + twosteps

        return rec(n)