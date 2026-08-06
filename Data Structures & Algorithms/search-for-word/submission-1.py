class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def rec(i, j, k):
            if k == len(word):
                return True
            
            if i < 0 or i >= len(board) \
             or j < 0 or j >= len(board[i]) \
             or (i,j) in visited:
                return False
            
            if board[i][j] == word[k]:
                visited.add((i, j))
                res = rec(i+1,j,k+1) \
                 or rec(i-1,j,k+1) \
                 or rec(i,j+1,k+1) \
                 or rec(i,j-1,k+1)
                visited.remove((i, j))
                return res
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if rec(i, j, 0):
                    return True
        
        return False

        