class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != 'L':
                return
            grid[x][y] = 'W'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        island_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'L':
                    dfs(i, j)
                    island_count += 1

        return island_count
