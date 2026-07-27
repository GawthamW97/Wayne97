class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1

        while l < r:
            m = (l + r) //2
            if nums[m] > nums[r]:
                # the min value is strictly to right
                l = m + 1
            else:
                # m may be the min value, hence we keep it in the search range
                r = m
        return nums[l]
