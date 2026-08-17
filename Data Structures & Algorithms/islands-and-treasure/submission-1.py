from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid), len(grid[0])
        visits = set()
        q = deque()

        def addCell(r,c): # the function will add the row and col ,to q and the visit for next iteration
            if r < 0 or c < 0 or c == cols or r == rows or grid[r][c] == -1 or (r,c) in visits:
                return
            visits.add((r,c))
            q.append([r,c])

        for row in range(rows): # first the treasure cells are added to the q
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append([row,col])
                    visits.add((row,col))
        
        dist = 0

        while q:
            for i in range(len(q)):
                r,c = q.popleft() # each for loop iteration will have an increment by 1 from the previous cell

                grid[r][c] = dist

                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)

            dist += 1