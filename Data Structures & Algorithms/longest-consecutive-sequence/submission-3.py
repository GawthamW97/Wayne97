class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = set()
        maxLen = 1
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            if len(ans) == 0:
                ans.add(nums[i])
                continue

            if nums[i] == nums[i-1]:
                continue 

            if nums[i] - 1 != nums[i-1]:
                ans = set()

            ans.add(nums[i])
            maxLen = max(maxLen,len(ans))
        return maxLen