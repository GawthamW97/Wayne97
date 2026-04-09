class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = 1
        maxContainer = 0
        while left != n - 1:
            minHeight = min(heights[right],heights[left])
            maxContainer = max(maxContainer, (right - left)  * minHeight)
            right += 1
            if right > n - 1:
                left += 1
                right = left + 1
        return maxContainer