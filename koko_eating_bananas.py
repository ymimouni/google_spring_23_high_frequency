import math

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_, max_ = 1, max(piles)

        while min_ < max_:
            mid = (min_ + max_) // 2
            h_spent = 0

            for pile in piles:
                h_spent += math.ceil(pile / mid)

            if h_spent <= h:
                max_ = mid
            else:
                min_ = mid + 1

        return min_
