from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(row, col):
            grid[row][col] = -1

            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for d in directions:
                new_r, new_c = row + d[0], col + d[1]
                if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == 1:
                    dfs(new_r, new_c)

        for col in range(n):
            if grid[0][col] == 1:
                dfs(0, col)
            if grid[m - 1][col] == 1:
                dfs(m - 1, col)

        for row in range(m):
            if grid[row][0] == 1:
                dfs(row, 0)
            if grid[row][n - 1] == 1:
                dfs(row, n - 1)

        ans = sum(1 for row in range(m) for col in range(n) if grid[row][col] == 1)

        for row in range(m):
            for col in range(n):
                grid[row][col] = 1 if grid[row][col] == -1 else grid[row][col]

        return ans
