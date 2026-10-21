class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i - 1]:
                continue
            l,r = i + 1,n - 1
            while l < r:
                val = nums[l] + nums[i] + nums[r]
                if val > 0:
                    r -= 1
                elif val < 0:
                    l += 1
                else:
                    ans.append([nums[l],nums[i],nums[r]])
                    l +=1
                    r -=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return ans