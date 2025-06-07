import math

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        flag = False
        min_, max_ = math.inf, -math.inf
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                flag = True
            if flag:
                min_ = min(min_, nums[i + 1])

        flag = False
        for i in range(n - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                flag = True
            if flag:
                max_ = max(max_, nums[i - 1])

        left, right = 0, n - 1
        while left < n:
            if nums[left] > min_:
                break
            left += 1

        while right >= 0:
            if nums[right] < max_:
                break
            right -= 1

        return right - left + 1 if right > left else 0


# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         n = len(nums)
#         stack = []
#         left, right = len(nums), -1
#         for i in range(n):
#             while stack and nums[i] < nums[stack[-1]]:
#                 left = min(left, stack.pop())
#             stack.append(i)

#         stack.clear()
#         for i in range(n - 1, -1, -1):
#             while stack and nums[i] > nums[stack[-1]]:
#                 right = max(right, stack.pop())
#             stack.append(i)

#         return right - left + 1 if right != -1 else 0
