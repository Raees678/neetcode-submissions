class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        # you havent found the target yet
        # r tells the idx of largest element that is smaller than the target
        
        # there is no element smaller than the target
        # meaning no row starts with a number smaller than the target
        # so target does not exist
        if r == -1:
            return False
        
        col_l = 0
        col_r = len(matrix[r]) - 1
        
        while col_l <= col_r:
            col_mid = (col_l + col_r) // 2
            if matrix[r][col_mid] == target:
                return True
            elif matrix[r][col_mid] < target:
                col_l = col_mid + 1
            else:
                col_r = col_mid - 1

        return False
        
