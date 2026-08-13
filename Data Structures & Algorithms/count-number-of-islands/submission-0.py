class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if rows <= row or row < 0 or cols <= col or col < 0 or grid[row][col] != '1':
                return

            grid[row][col] = '0'

            dfs(row, col+1)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row-1, col)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1

        return islands