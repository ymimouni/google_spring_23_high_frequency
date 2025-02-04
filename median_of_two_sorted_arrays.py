from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        left1, right1 = 0, m
        while left1 <= right1:
            partition1 = (left1 + right1) // 2
            partition2 = (m + n + 1) // 2 - partition1

            max_left1 = nums1[partition1 - 1] if partition1 > 0 else float("-inf")
            min_right1 = nums1[partition1] if partition1 < m else float("inf")
            max_left2 = nums2[partition2 - 1] if partition2 > 0 else float("-inf")
            min_right2 = nums2[partition2] if partition2 < n else float("inf")

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (m + n) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return max(max_left1, max_left2)
            elif max_left2 > min_right1:
                left1 = partition1 + 1
            else:
                right1 = partition1 - 1


# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         m, n = len(nums1), len(nums2)
#         left1, right1 = 0, m - 1
#         left2, right2 = 0, n - 1

#         def helper(left1: int, right1: int, left2: int, right2: int, idx: int) -> int:
#             if left1 > right1:
#                 return nums2[idx - left1]
#             elif left2 > right2:
#                 return nums1[idx - left2]

#             mid1 = (left1 + right1) // 2
#             mid2 = (left2 + right2) // 2

#             # If idx is in the right half of nums1 + nums2, remove the smaller left half.
#             if mid1 + mid2 < idx:
#                 if nums1[mid1] < nums2[mid2]:
#                     return helper(mid1 + 1, right1, left2, right2, idx)
#                 else:
#                     return helper(left1, right1, mid2 + 1, right2, idx)
#             # Otherwise, remove the larger right half.
#             else:
#                 if nums1[mid1] < nums2[mid2]:
#                     return helper(left1, right1, left2, mid2 - 1, idx)
#                 else:
#                     return helper(left1, mid1 - 1, left2, right2, idx)

#         if (m + n) % 2 == 0:
#             return (helper(0, m - 1, 0, n - 1, (m + n - 1) // 2) + helper(0, m - 1, 0, n - 1, (m + n) // 2)) / 2
#         else:
#             return helper(0, m - 1, 0, n - 1, (m + n) // 2)


# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         m, n = len(nums1), len(nums2)
#         p1 = p2 = 0

#         def get_min():
#             nonlocal p1, p2
#             if p1 == m:
#                 ans = nums2[p2]
#                 p2 += 1
#             elif p2 == n:
#                 ans = nums1[p1]
#                 p1 += 1
#             elif nums1[p1] <= nums2[p2]:
#                 ans = nums1[p1]
#                 p1 += 1
#             else:
#                 ans = nums2[p2]
#                 p2 += 1
#             return ans

#         if (m + n) % 2 == 0:
#             for _ in range((m + n - 1) // 2):
#                 _ = get_min()
#             return (get_min() + get_min()) / 2
#         else:
#             for _ in range((m + n) // 2):
#                 _ = get_min()
#             return get_min()
