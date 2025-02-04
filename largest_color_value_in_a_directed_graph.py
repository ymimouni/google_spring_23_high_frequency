from collections import defaultdict, Counter
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for (from_, to) in edges:
            graph[from_].append(to)

        dp = defaultdict(Counter)

        seen = set()

        def dfs(vertex: int) -> int:
            if dp[vertex]:
                return max(dp[vertex].values())

            if vertex in seen:
                return -1

            seen.add(vertex)
            if vertex in graph:
                for next_v in graph[vertex]:
                    if dfs(next_v) == -1:
                        return -1

                for neighbor in graph[vertex]:
                    partial = dp[neighbor]
                    dp[vertex] |= partial

            dp[vertex][colors[vertex]] += 1
            seen.remove(vertex)
            return max(dp[vertex].values())

        largest_v = -1
        for head in graph.keys():
            largest_v = max(largest_v, dfs(head))

        return largest_v if edges else 1
