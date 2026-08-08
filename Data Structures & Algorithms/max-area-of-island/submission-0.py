class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        curr = res = 0
        def dfs(i, j):
            nonlocal curr
            if i < 0 or i >= len(grid):
                return
            if j < 0 or j >= len(grid[i]):
                return
            if (i,j) in visited or not grid[i][j]:
                return
            
            visited.add((i,j))
            curr += 1
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in visited and grid[i][j]:
                    dfs(i,j)
                    res = max(res, curr)
                    curr = 0

        return res
        

