class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(row_idx):
            s = set()
            for i in board[row_idx]:
                if i in s and i != ".":
                    return False
                else:
                    s.add(i)
            
            return True

        def checkCol(col_idx):
            s = set()
            for row_idx in range(len(board)):
                if board[row_idx][col_idx] in s and board[row_idx][col_idx] != ".":
                    return False
                else:
                    s.add(board[row_idx][col_idx])
            
            return True
        
        def checkSquare(rows, cols):
            s = set()
            for row in rows:
                for col in cols:
                    if board[row][col] in s and board[row][col] != ".":
                        return False
                    else:
                        s.add(board[row][col])
            
            return True
        
        for row in range(0, 9):
            if not checkRow(row):
                return False
        
        for col in range(0, 9):
            if not checkCol(col):
                return False
        
        rows = [[0,1,2], [3,4,5], [6,7,8]]
        cols = [[0,1,2], [3,4,5], [6,7,8]]
        for row in rows:
            for col in cols:
                if not checkSquare(row, col):
                    return False
        
        return True
        


        
