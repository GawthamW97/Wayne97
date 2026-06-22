class Solution:
    def trap(self, height: List[int]) -> int:
        totalArea = 0
        area = 0
        l, r = 0, len(height) - 1

        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax,height[l])
                area = leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                area = rightMax - height[r]
            totalArea = totalArea + area
        
        return totalArea