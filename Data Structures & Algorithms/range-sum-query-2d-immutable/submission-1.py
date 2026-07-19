class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.sums = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                up = self.sums[i - 1][j] if i > 0 else 0
                left = self.sums[i][j - 1] if j > 0 else 0
                dup = self.sums[i - 1][j - 1] if i > 0 and j > 0 else 0
                el = matrix[i][j]
                self.sums[i][j] = el + up + left - dup

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        up = self.sums[row1 - 1][col2] if row1 > 0 else 0
        left = self.sums[row2][col1 - 1] if col1 > 0 else 0
        dup = self.sums[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        total = self.sums[row2][col2]

        return total - up - left + dup
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)