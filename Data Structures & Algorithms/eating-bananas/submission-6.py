import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r= 0,max(piles) # left will be the zero and right will be max number of bananas  

        minK = r # initial minimum K will the max number of banana in the piles

        while l <= r: 
            m = (l + r) // 2 # get the average banana between left and right pointer

            if m == 0:  # if the avg is zero that means the left and right are zero position
                break   # we break the look since zero avg is not a possible outcome

            tempK = sum([math.ceil(x / m) for x in piles]) #get the total time it takes to consume each piles

            if tempK <= h: # if the total time taken is less than the h we update the minK and move the right pointer to 
                minK = min(minK,m)
                r = m - 1
            else:
                l = m + 1 # if the tempK is more than h, we will move the left pointer
        return minK
