class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visit = set()
        def dfs(row,col):
            if (row < 0 or row == rows or col < 0 or
                col == cols or grid[row][col] == 0 or
                (row, col) in visit
            ):
                return 0
            
            visit.add((row,col))

            return (1 + dfs(row + 1,col)
            +dfs(row - 1,col)
            +dfs(row, col + 1)
            +dfs(row,col - 1))

        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == 1):
                    maxArea = max(dfs(i,j),maxArea)
        return maxArea


