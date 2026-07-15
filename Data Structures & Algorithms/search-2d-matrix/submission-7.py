class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        rowL = 0
        rowR = ROWS - 1
        targetRowIndex = 0
        while rowL <= rowR:
            rowM = (rowR + rowL) // 2
            if matrix[rowM][0] > target:
                rowR = rowM - 1
            elif matrix[rowM][-1] < target:
                rowL = rowM + 1
            else:
                break
        if rowL > rowR:
            return False
        colL = 0
        colR = COLS - 1
        targetRowIndex = (rowR + rowL) //2
        while colL <= colR:
            colM = (colR - colL) // 2 + colL
            if matrix[targetRowIndex][colM] > target:
                colR = colM - 1
            elif matrix[targetRowIndex][colM] < target:
                colL = colM + 1
            else:
                return True
        return False
            