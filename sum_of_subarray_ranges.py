from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        stack = []
        ans = 0
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                ans -= nums[mid] * (mid - left) * (right - mid)
            stack.append(right)

        stack.clear()
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                left = stack[-1] if stack else -1
                ans += nums[mid] * (mid - left) * (right - mid)
            stack.append(right)

        return ans

    # def subArrayRanges(self, nums: List[int]) -> int:
    #     n = len(nums)

    #     ans = 0
    #     for start in range(n):
    #         min_ = max_ = nums[start]
    #         for end in range(start, n):
    #             min_ = min(min_, nums[end])
    #             max_ = max(max_, nums[end])
    #             ans += (max_ - min_)

    #     return ans
