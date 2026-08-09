class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r, c = len(board), len(board[0])

        visited = set()
        def dfs(i, j):
            if i < 0 or i >= r:
                return
            if j < 0 or j >= c:
                return
            if board[i][j] == "X":
                return
            if (i, j) in visited:
                return
            
            visited.add((i, j))
            dfs(i+1, j) 
            dfs(i-1, j) 
            dfs(i, j+1) 
            dfs(i, j-1)
            return
        
        for i in range(c):
            dfs(0, i)
            dfs(r-1, i)
        for i in range(r):
            dfs(i, 0)
            dfs(i,c-1)
        
        for i in range(r):
            for j in range(c):
                if (i,j) not in visited:
                    board[i][j] = "X"
        
        return
        
            
