import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 0,max(piles)
        minK = r
        while l <= r:
            m = l + (r-l)//2
            if m == 0:
                break
            tempK = sum([math.ceil(x / m) for x in piles])
            if tempK <= h:
                minK = min(m,minK)
                r = m - 1
            else:
                l = m + 1
        return minK

