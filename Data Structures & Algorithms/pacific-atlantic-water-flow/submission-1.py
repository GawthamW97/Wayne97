class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pac = set()
        atl = set()

        def dfs(r,c,height,visit):
            if r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < height or (r,c) in visit:
                return
            visit.add((r,c))
            dfs(r + 1,c,heights[r][c],visit)
            dfs(r - 1,c,heights[r][c],visit)
            dfs(r,c + 1,heights[r][c],visit)
            dfs(r,c - 1,heights[r][c],visit)

        
        for c in range(cols):
            dfs(0,c,heights[0][c],pac)
            dfs(rows - 1,c,heights[rows - 1][c],atl)
        
        for r in range(rows):
            dfs(r,0,heights[r][0],pac)
            dfs(r,cols - 1,heights[r][cols - 1],atl)

        
        return [x for x in pac if x in atl]



