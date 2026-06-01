class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        def recurse(i,ds):
            if i >= len(nums):
                res.append(ds.copy())
                return
            ds.append(nums[i])
            recurse(i+1,ds)
            ds.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            recurse(i+1,ds)
        recurse(0,[])
        return res