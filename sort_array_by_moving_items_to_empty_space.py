from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> int:
        def helper(nums: List[int], offset: int) -> int:
            ops = 0
            for (i, num) in enumerate(nums):
                # If num is zero or is in the right position, skip it.
                if num == 0 or num == i + offset:
                    continue
                ops += 1

                # Detect cycles.
                j = i
                while nums[j] > 0:
                    # Mark num as visited.
                    nums[j] = -nums[j]
                    j = -nums[j] - offset

                    if j == i:
                        # We found a cycle.
                        ops += 1
                        break

            for (i, num) in enumerate(nums):
                nums[i] = -num if num < 0 else num

            return ops

        return min(helper(nums, 0), helper(nums, 1))
