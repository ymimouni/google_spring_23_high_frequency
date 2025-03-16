import math
from collections import defaultdict

from typing import List


class Solution:
    """
    Using Sparse Tables.
    """

    class MST:
        def __init__(self, table: List[int]) -> None:
            N = len(table)
            K = int(math.log2(N)) + 1
            self.st = [[0] * N for _ in range(K)]
            self.table = table

            for idx in range(N):
                self.st[0][idx] = idx

            for k in range(1, K):
                for i in range(N - (1 << k) + 1):
                    left = self.st[k - 1][i]
                    right = self.st[k - 1][i + (1 << (k - 1))]
                    self.st[k][i] = left if table[left] <= table[right] else right

        def get_min_index(self, start: int, end: int) -> int:
            if start > end:
                start, end = end, start
            k = int(math.log2(end - start + 1))
            left = self.st[k][start]
            right = self.st[k][end - (1 << k) + 1]
            return left if self.table[left] <= self.table[right] else right

    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        tree = defaultdict(list)

        for start, end in edges:
            tree[start].append(end)
            tree[end].append(start)

        m = len(edges)  # number of edges.
        euler = []
        depth = []
        first = [0] * n
        seen = set()

        def dfs(node: int, curr_d: int = 0) -> None:
            seen.add(node)
            first[node] = len(euler)
            euler.append(node)
            depth.append(curr_d)
            for child in tree[node]:
                if child not in seen:
                    dfs(child, curr_d + 1)
                    euler.append(node)
                    depth.append(curr_d)

        dfs(node=0)
        mst = self.MST(table=depth)
        ans = []
        for (start, end, node) in query:
            start_f, end_f, node_f = first[start], first[end], first[node]
            c1 = mst.get_min_index(start_f, end_f)
            c2 = mst.get_min_index(start_f, node_f)
            c3 = mst.get_min_index(node_f, end_f)
            c = max(c1, c2, c3, key=lambda x: depth[x])
            ans.append(euler[c])

        return ans


# class Solution:
#     """
#     Using Binary Lifting.
#     """
#     def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
#         tree = defaultdict(list)

#         for (start, end) in edges:
#             tree[start].append(end)
#             tree[end].append(start)

#         parent = [0] * n
#         depth = [0] * n
#         seen = set()
#         def dfs(parent_n: int, node: int, cur_d: int = 0) -> None:
#             seen.add(node)
#             depth[node] = cur_d
#             parent[node] = parent_n
#             for child in tree[node]:
#                 if child not in seen:
#                     dfs(node, child, cur_d + 1)

#         # Parent of node 0 is itself.
#         dfs(0, 0, 0)

#         K = int(math.log2(n)) + 1
#         dp = [[0] * n for _ in range(K)]

#         dp[0][:] = parent[:]

#         for k in range(1, K):
#             for i in range(n):
#                 prev = dp[k-1][i]
#                 dp[k][i] = dp[k-1][prev]

#         def lca(p: int, q: int) -> int:
#             """
#             Return the Lowest Common Ancestor.
#             """
#             if depth[p] > depth[q]:
#                 p, q = q, p

#             # Move q to the level of p.
#             k = depth[q] - depth[p]
#             while k > 0:
#                 i = int(math.log2(k))
#                 q = dp[i][q]
#                 k -= (1 << i)

#             if p == q:
#                 return p

#             # Move p and q to the nodes just below the LCA.
#             k = K
#             while k > 0:
#                 i = int(math.log2(k))
#                 if dp[i][p] != dp[i][q]:
#                     p = dp[i][p]
#                     q = dp[i][q]
#                 k -= 1
#             return parent[p]

#         ans = []
#         for (start, end, node) in query:
#             c1 = lca(start, end)
#             c2 = lca(end, node)
#             c3 = lca(start, node)
#             c = max(c1, c2, c3, key=lambda x: depth[x])
#             ans.append(c)

#         return ans


# class Solution:
#     def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
#         graph = defaultdict(list)

#         for start, end in edges:
#             graph[start].append(end)
#             graph[end].append(start)

#         path = []
#         seen = set()
#         found = False
#         def dfs_path(node: int, end: int) -> None:
#             nonlocal found

#             if found or node in seen:
#                 return None
#             seen.add(node)

#             path.append(node)

#             if node == end:
#                 found = True
#                 return None

#             for neighbor in graph[node]:
#                 dfs_path(neighbor, end)

#             if not found:
#                 path.pop()

#         distance = {}
#         def dfs_dist(node: int, dist: int = 0) -> None:
#             if node in distance:
#                 return None

#             distance[node] = dist

#             for neighbor in graph[node]:
#                 dfs_dist(neighbor, dist + 1)

#         ans = []
#         for (start, end, node) in query:
#             dfs_path(start, end)
#             dfs_dist(node)

#             min_dist = inf
#             for p_node in path:
#                 if distance[p_node] < min_dist:
#                     closest = p_node
#                     min_dist = distance[p_node]
#             ans.append(closest)

#             path.clear(); seen.clear(); distance.clear(); found = False

#         return ans


# class Solution:
#     def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
#         graph = defaultdict(list)
#         for (start, end) in edges:
#             graph[start].append(end)
#             graph[end].append(start)

#         path = []
#         seen = set()
#         found = False
#         def dfs_path(node: int, end: int) -> None:
#             nonlocal found

#             if found or node in seen:
#                 return None

#             seen.add(node)
#             path.append(node)
#             if node == end:
#                 found = True
#                 return None

#             for neighbor in graph[node]:
#                 dfs_path(neighbor, end)

#             if not found:
#                 path.pop()

#         distance = {}
#         def dfs_dist(node, current) -> None:
#             if node in distance:
#                 return None

#             distance[node] = current

#             for neighbor in graph[node]:
#                 dfs_dist(neighbor, current + 1)

#         ans = []
#         for (start, end, node) in query:
#             dfs_path(start, end)
#             dfs_dist(node, 0)

#             min_ = inf
#             for p_node in path:
#                 p_dist = distance[p_node]
#                 if p_dist < min_:
#                     closest = p_node
#                     min_ = p_dist
#             ans.append(closest)

#             path.clear()
#             seen.clear()
#             distance.clear()
#             found = False

#         return ans
