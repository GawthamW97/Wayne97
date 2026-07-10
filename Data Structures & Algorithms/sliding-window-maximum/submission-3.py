from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        q = deque()
        output = []

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # remove index of number lower than the current number
                q.pop()
            
            q.append(r) # add indices to queue

            if l > q[0]: # if the left index is higher than the left most index in the q
                q.popleft() # it means the window was slided by 1 index and we need to remove the old left index from queue

            if r + 1 >= k: # if the window reaches the k length then 
                output.append(nums[q[0]]) # we add the max element within the window, which is the element under left most index in queue.
                l+=1 # once added we slide the window by 1 element
            r += 1
        return output