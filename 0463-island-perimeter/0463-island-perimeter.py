class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        land = 0
        shared = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    land += 1
                    if i > 0 and grid[i - 1][j]:
                        shared += 1
                    if j > 0 and grid[i][j - 1]:
                        shared += 1
        return land * 4 - shared * 2