class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        maxNum = 0
        for i in range(n):
            leftMax[i] = maxNum
            maxNum = max(height[i],maxNum)
        maxNum = 0
        for i in range(n-1,-1,-1):
            rightMax[i] = maxNum
            maxNum = max(height[i],maxNum)
        totalWater = 0

        for i in range(n):
            calc = min(leftMax[i],rightMax[i]) - height[i]
            if calc > 0:
                totalWater+= calc
        
        return totalWater
