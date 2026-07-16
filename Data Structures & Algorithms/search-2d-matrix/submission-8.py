class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0,COLS - 1
        top, bot = 0, ROWS - 1
        mid = 0
        while top <= bot:
            mid = (top+bot)//2
            if (matrix[mid][0] > target):
                bot = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        
        if top > bot:
            return False
        
        mid = (top + bot) // 2
        while l <= r:
            secMid = (l + r) // 2

            if matrix[mid][secMid] < target:
                l = secMid + 1
            elif matrix[mid][secMid] > target:
                r = secMid - 1
            else:
                return True

        return False