class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0 ,len(nums) - 1
        minNum = nums[l]

        while l <= r:
            if nums[l] <= nums[r]:
                minNum = min(minNum,nums[l])
                break
            m = (l + r) // 2
            minNum = min(nums[m],minNum)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return minNum
#nums = [2,1]
#l=0,r=0,m=0,num[l],num[r],num[m]
#l=0,r=1,m=0,num[l]=2,num[r]=1,num[m]=2

               