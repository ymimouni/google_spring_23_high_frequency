from math import inf
from typing import List


class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        # Sort by x-intercept, otherwise reverse y-intercept.
        sorted_p = sorted(peaks, key=lambda x: (x[0] - x[1], -(x[0] + x[1])))

        reach = -inf
        visible = 0
        for i, (x, y) in enumerate(sorted_p):
            if x + y > reach:
                reach = x + y

                # Duplicates should not count.
                if i < len(peaks) - 1 and sorted_p[i] == sorted_p[i + 1]:
                    continue

                visible += 1

        return visible

    # def visibleMountains(self, peaks: List[List[int]]) -> int:
    #     def within(peak_1: List[int], peak_2: List[int]) -> bool:
    #         x_1, y_1 = peak_1
    #         x_2, y_2 = peak_2
    #         return y_1 <= y_2 and abs(x_2 - x_1) <= abs(y_2 - y_1)

    #     sorted_p = sorted(peaks)
    #     seen = set()
    #     stack = []
    #     for peak in sorted_p:
    #         if stack and stack[-1] == peak:
    #             seen.add(tuple(peak))
    #             continue

    #         while stack and within(stack[-1], peak):
    #             stack.pop()
    #         if not stacrk or not within(peak, stack[-1]):
    #             stack.append(peak)

    #     return len(stack) - len(seen)

    # def visibleMountains(self, peaks: List[List[int]]) -> int:
    #     def is_visible_through(peak_1: List[int], peak_2: List[int]) -> bool:
    #         x_1, y_1 = peak_1
    #         x_2, y_2 = peak_2
    #         return y_1 > y_2 or abs(x_2 - x_1) > abs(y_2 - y_1)

    #     visible_mountains = 0
    #     for (i, peak_1) in enumerate(peaks):
    #         for (j, peak_2) in enumerate(peaks):
    #             if i != j and not is_visible_through(peak_1, peak_2):
    #                 break
    #         else:
    #             visible_mountains += 1

    #     return visible_mountains
