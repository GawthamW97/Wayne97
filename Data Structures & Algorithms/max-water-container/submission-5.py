class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        maxContainer = 0
        while left < right:
            area = (right - left) * min(heights[left],heights[right])
            maxContainer = max(maxContainer,area)
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1
        return maxContainer