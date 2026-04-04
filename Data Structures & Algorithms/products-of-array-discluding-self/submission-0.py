class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        left = 0
        right = 1
        total = 1

        while left < len(nums):
            total *= nums[right]
            right = (right+1) % len(nums)
            if right == left:
                ans.append(total)
                total = 1
                left += 1
                right = (left + 1) % len(nums)
        return ans