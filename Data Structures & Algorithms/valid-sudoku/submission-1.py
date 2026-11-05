class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for i in range((len(board))):
            for j in range(len(board[i])):
                el = board[i][j]
                square_idx = (i // 3, j // 3)
                if el != "." and (el in row[i] or el in col[j] or el in square[square_idx]):
                    return False
                row[i].add(el)
                col[j].add(el)
                square[square_idx].add(el)
        
        return True