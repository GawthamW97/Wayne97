class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = []
        l, r = 0, k - 1
        while r < len(nums):
            window.append(max(nums[l:r+1]))
            r += 1
            l += 1

        return window