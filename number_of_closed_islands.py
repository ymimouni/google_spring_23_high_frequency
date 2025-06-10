from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(row: int, col: int) -> None:
            grid[row][col] = -1

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for d in directions:
                new_r, new_c = row + d[0], col + d[1]
                if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == 0:
                    dfs(new_r, new_c)

        for col in range(n):
            # First row.
            if grid[0][col] == 0:
                dfs(0, col)
            # Last row.
            if grid[m - 1][col] == 0:
                dfs(m - 1, col)

        for row in range(m):
            # First column.
            if grid[row][0] == 0:
                dfs(row, 0)
            # Last column.
            if grid[row][n - 1] == 0:
                dfs(row, n - 1)

        islands = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    islands += 1
                    dfs(row, col)

        for row in range(m):
            for col in range(n):
                grid[row][col] = 0 if grid[row][col] == -1 else grid[row][col]

        return islands
