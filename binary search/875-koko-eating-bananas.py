from ast import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            k = (l + r) // 2
            total_hours = sum(math.ceil(pile / k) for pile in piles)
            if total_hours <= h:
                r = k - 1
            else:
                l = k + 1
        return l