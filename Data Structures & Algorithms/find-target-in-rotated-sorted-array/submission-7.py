class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0,len(nums) - 1
        while l <= r:
            m = l + (r-l)//2
            print(nums[l],nums[r],nums[m])
            if nums[m] == target:
                return m
            elif nums[m] > target:
                if nums[l] <= target or nums[m] < nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[r] >= target or nums[m] > nums[r]:
                    l = m + 1 
                else:
                    r = m - 1
        return - 1
# [4,5,6,7,0,1,2] , 0
# 4,2,7
# 0,2,1
# 0,1,0