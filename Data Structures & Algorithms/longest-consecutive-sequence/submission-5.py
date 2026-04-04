class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        curr = 0
        count = 0
        maxLen = 0
        for num in (numSet):
            if num - 1 not in numSet:
                curr = num
                count = 1
                while curr + 1 in numSet:
                    curr += 1
                    count += 1
                maxLen = max(maxLen,count)
        return maxLen