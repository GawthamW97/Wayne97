class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left ,right = i+1, n - 1
            while left < right:
                three_sum = nums[left] + nums[right] + nums[i]
                if three_sum == 0:
                    ans.append([nums[left],nums[right],nums[i]])
                    left+=1
                    while nums[left] == nums[left -1] and left < right:
                        left+=1
                elif three_sum > 0:
                    right-=1
                else:
                    left+=1

        return ans
