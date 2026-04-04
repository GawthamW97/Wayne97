class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        curr = 0
        count = 0
        maxLen = 0
        for num in (numSet):
            if count == 0 and num - 1 not in numSet:
                curr = num
                count = 1
            else:
                continue
            
            while curr + 1 in numSet:
                curr += 1
                count += 1
            maxLen = max(maxLen,count)
            count = 0
        return maxLen