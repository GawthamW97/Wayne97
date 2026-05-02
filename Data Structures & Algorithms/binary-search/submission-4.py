class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0, n - 1
        while l <= r:
            pos = (r - l) // 2 + l
            if nums[pos] < target:
                l = pos + 1
            elif nums[pos] > target:
                r = pos - 1
            else:
                return pos
        return -1
