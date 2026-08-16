from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def inbounds(i, j):
            return 0 <= i < m and 0 <= j < n and (i,j) not in visiting
        
        visiting = set()

        @cache
        def rec(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            
            visiting.add((i,j))
            res = 0
            if inbounds(i+1,j):
                res += rec(i+1, j)
            if inbounds(i,j+1):
                res += rec(i,j+1)
            visiting.remove((i,j))
            
            return res
        
        return rec(0,0)


        