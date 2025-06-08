import heapq

from typing import List


class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        min_heap = []
        for row in range(m):
            for col in range(n):
                heapq.heappush(min_heap, (grid[row][col], row, col))

        rows = [0] * m
        cols = [0] * n

        i = 0
        while min_heap:
            (_, row, col) = heapq.heappop(min_heap)
            current = max(rows[row], cols[col]) + 1
            grid[row][col] = current
            rows[row] = cols[col] = current

        return grid


# class Solution:
#     def minScore(self, grid: List[List[int]]) -> List[List[int]]:
#         m, n = len(grid), len(grid[0])

#         nums = [(grid[row][col], row, col) for row in range(m) for col in range(n)]
#         nums.sort()

#         rows = [0] * m
#         cols = [0] * n

#         i = 0
#         for (_, row, col) in nums:
#             current = max(rows[row], cols[col]) + 1
#             grid[row][col] = current
#             rows[row] = cols[col] = current

#         return grid
