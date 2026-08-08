class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]
        row_positions = set()
        col_positions = set()
        pos_diagonals = set()
        neg_diagonals = set()

        def possible(i, j):
            if i in row_positions or j in col_positions:
                return False
            if i + j in pos_diagonals:
                return False
            if i + (n - 1 - j) in neg_diagonals:
                return False
            return True


        # i is a row index
        def place(i, queens):
            # if you are out of queens record the soln
            if queens == 0:
                soln = ["".join(row) for row in board]
                res.append(soln)
                return
            
            # if you are not yet out of queens
            # but youve run out of rows to place you cant 
            # do anything more
            if i >= n:
                return
            
            # try to place a queen in every col in row i
            for j in range(n):
                if possible(i, j):
                    board[i][j] = "Q"
                    row_positions.add(i)
                    col_positions.add(j)
                    pos_diagonals.add(i+j)
                    neg_diagonals.add(i + (n - 1 - j))
                    place(i+1,queens-1)
                    row_positions.remove(i)
                    col_positions.remove(j)
                    pos_diagonals.remove(i+j)
                    neg_diagonals.remove(i + (n - 1 - j))
                    board[i][j] = "."
        
        place(0, n)
        return res
                    




            

        