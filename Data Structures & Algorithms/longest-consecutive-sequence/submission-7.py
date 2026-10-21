class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        count = 0 #count of element
        curr = 0 #current element
        maxSize = 0 #max size of the sub-array
        
        for num in numSet:
            if num - 1 not in numSet:
                curr = num
                count = 1
                while curr + 1 in numSet:
                    curr += 1
                    count += 1
                maxSize = max(maxSize,count)
        return maxSize