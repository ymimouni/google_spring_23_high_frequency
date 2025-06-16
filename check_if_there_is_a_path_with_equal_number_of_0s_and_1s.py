from typing import List


class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        if (m + n) % 2 == 0:
            return False

        min_path = [[0] * n for _ in range(m)]
        max_path = [[0] * n for _ in range(m)]

        min_path[0][0] = max_path[0][0] = grid[0][0]

        for row in range(m):
            for col in range(n):
                if row >= 1 and col >= 1:
                    min_path[row][col] = min(min_path[row - 1][col], min_path[row][col - 1]) + grid[row][col]
                    max_path[row][col] = max(max_path[row - 1][col], max_path[row][col - 1]) + grid[row][col]
                elif row >= 1:
                    min_path[row][col] = min_path[row - 1][col] + grid[row][col]
                    max_path[row][col] = max_path[row - 1][col] + grid[row][col]
                elif col >= 1:
                    min_path[row][col] = min_path[row][col - 1] + grid[row][col]
                    max_path[row][col] = max_path[row][col - 1] + grid[row][col]

        return min_path[m - 1][n - 1] <= (m + n - 1) // 2 <= max_path[m - 1][n - 1]


# class Solution:
#     def isThereAPath(self, grid: List[List[int]]) -> bool:
#         m, n = len(grid), len(grid[0])

#         if (m + n) % 2 == 0:
#             return False

#         dp = [[set() for _ in range(n)] for _ in range(m)]
#         dp[m-1][n-1].add(-1 if grid[m-1][n-1] == 0 else 1)

#         for row in range(m-1, -1, -1):
#             for col in range(n-1, -1, -1):
#                 if (row, col) == (m-1, n-1):
#                     continue
#                 else:
#                     if row < m - 1:
#                         for diff in dp[row+1][col]:
#                             if abs(diff) <= row + col + 1:
#                                 dp[row][col].add((diff - 1) if grid[row][col] == 0 else (diff + 1))
#                     if col < n - 1:
#                         for diff in dp[row][col+1]:
#                             if abs(diff) <= row + col + 1:
#                                 dp[row][col].add((diff - 1) if grid[row][col] == 0 else (diff + 1))

#         return 0 in dp[0][0]


# class Solution:
#     def isThereAPath(self, grid: List[List[int]]) -> bool:
#         m, n = len(grid), len(grid[0])

#         found = False
#         def dfs(row: int, col: int, ones: int, zeros: int) -> None:
#             nonlocal found

#             if found:
#                 return None

#             if grid[row][col] == 0:
#                 zeros += 1
#             else:
#                 ones += 1

#             if (row, col) == (m - 1, n - 1) and ones == zeros:
#                 found = True

#             if row < m - 1:
#                 dfs(row + 1, col, ones, zeros)
#             if col < n - 1:
#                 dfs(row, col + 1, ones, zeros)

#         dfs(0, 0, 0, 0)
#         return found
