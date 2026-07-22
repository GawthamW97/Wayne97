import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 0 , max(piles)
        minK = right
        while left <= right:
            m = (left + right) // 2
            if m == 0:
                break
            tempK = sum([math.ceil(x/m) for x in piles])
            if tempK <= h:
                minK = min(m,minK)
                right = m - 1
            else:
                left = m + 1
        return minK