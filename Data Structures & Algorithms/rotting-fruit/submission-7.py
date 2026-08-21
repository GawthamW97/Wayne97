from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        q = deque()
        visits = set()
        self.fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append([row,col])
                    visits.add((row,col))
                if grid[row][col] == 1:
                    self.fresh += 1
        def updateCell(r,c):
            if r < 0 or c < 0 or c == cols or r == rows or grid[r][c] == 0 or (r,c) in visits:
                return
            visits.add((r,c))
            q.append([r,c])
            self.fresh -= 1

        count = 0

        while self.fresh > 0 and q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2
                updateCell(r+1,c)
                updateCell(r-1,c)
                updateCell(r,c+1)
                updateCell(r,c-1)
            count+=1

        return count if self.fresh == 0 else -1
