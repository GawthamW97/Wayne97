class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = [] #output window
        l, r = 0, k - 1 # initialize the pointers
        while r < len(nums):
            window.append(max(nums[l:r+1])) # get the max value of each window
            r += 1  #increment r and l pointer
            l += 1

        return window