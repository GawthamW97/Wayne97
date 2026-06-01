class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        def recurse(i,ds):
            res.append(ds.copy())
            for j in range(i,len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                ds.append(nums[j])
                recurse(j+1,ds)
                ds.pop()

        recurse(0,[])
        return res





