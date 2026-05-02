class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l,r= 0 , m - 1
        for row in matrix:
            if row[r] == target:
                return True
            elif row[r] > target:
                while l <= r:
                    pos = l + (r - l) //2
                    if row[pos] > target:
                        r = pos - 1
                    elif row[pos] < target:
                        l = pos + 1
                    else:
                        return True
        
        return False