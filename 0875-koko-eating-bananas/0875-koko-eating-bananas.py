import numpy as np

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def number_hours(piles, k):
            hours = 0
            for pile in piles:
                hours += int(np.ceil(pile / k))
            return hours

        l = 1
        r = max(piles)
        m = (l + r) // 2

        if  m == 1:
            if number_hours(piles, m) > h:
                return r
            else:
                return l
        elif len(piles) >= 2:
            while m > l:
                if number_hours(piles, m) <= h:
                    r = m
                    m = (l + r) // 2
                elif number_hours(piles, m) > h:
                    l = m
                    m = (l + r) // 2
            return m + 1
        else:
            return int(np.ceil(piles[0] / h))
        