from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for (from_, to) in tickets:
            graph[from_].append(to)

        for neighbors in graph.values():
            neighbors.sort(reverse=True)

        stack = ["JFK"]
        itinerary = []
        while stack:
            if graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            else:
                itinerary.append(stack.pop())

        return itinerary[::-1]


# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         graph = defaultdict(list)
#
#         for (from_, to) in tickets:
#             graph[from_].append(to)
#
#         for neighbors in graph.values():
#             neighbors.sort(reverse=True)
#
#         itinerary = []
#
#         def dfs(city: str) -> None:
#             while graph[city]:
#                 dfs(graph[city].pop())
#             itinerary.append(city)
#
#         dfs("JFK")
#
#         return itinerary[::-1]


# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         graph = defaultdict(list)
#         num_vertices = defaultdict(int)
#
#         for (from_, to) in tickets:
#             graph[from_].append(to)
#             num_vertices[(from_, to)] += 1
#
#         solution = []
#         current = []
#
#         def dfs(city: str) -> None:
#             nonlocal solution, current
#
#             current.append(city)
#             if len(current) == len(tickets) + 1:
#                 if not solution or ''.join(current) < ''.join(solution):
#                     solution = current[:]
#             for next_ in graph[city]:
#                 if num_vertices[(city, next_)] > 0:
#                     num_vertices[(city, next_)] -= 1
#                     dfs(next_)
#                     num_vertices[(city, next_)] += 1
#
#             current.pop()
#
#         dfs("JFK")
#
#         return solution
