class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if rows <= row or row < 0 or cols <= col or col < 0 or grid[row][col] != 1:
                return 0

            grid[row][col] = 0

            a = dfs(row, col+1)
            b = dfs(row+1, col)
            c = dfs(row, col-1)
            d = dfs(row-1, col)
            
            return 1 + a+b+c+d

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)

        return maxArea
