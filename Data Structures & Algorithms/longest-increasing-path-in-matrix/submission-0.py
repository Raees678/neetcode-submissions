from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def can_go(i, j, num):
            return 0 <= i < len(matrix) and 0 <= j < len(matrix[i]) and matrix[i][j] > num

        @cache
        def rec(i, j):
            num = matrix[i][j]
            u = d = l = r = 0
            if can_go(i+1, j, num):
                r = 1 + rec(i+1, j)
            if can_go(i-1, j, num):
                l = 1 + rec(i-1, j)
            if can_go(i, j+1, num):
                d = 1 + rec(i, j+1)
            if can_go(i, j-1, num):
                u = 1 + rec(i, j-1)
            
            return max(u,d,l,r)
        
        res = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                curr = 1 + rec(i, j)
                res = max(res, curr)
        
        return res
        

            
