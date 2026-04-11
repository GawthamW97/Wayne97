class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        leftMax = height[l]
        rightMax = height[r]
        totalWater = 0
        while l < r:
            if leftMax <= rightMax:
                l += 1
                calc = leftMax - height[l]
                leftMax = max(leftMax,height[l])
            else:
                r -=1
                calc = rightMax - height[r] 
                rightMax = max(rightMax,height[r])
            if calc > 0:
                totalWater = totalWater +  calc
        return totalWater
