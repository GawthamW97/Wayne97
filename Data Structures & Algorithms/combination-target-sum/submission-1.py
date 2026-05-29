class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        def dfs(i,ds,val):
            if val == target:
                res.append(ds.copy())
                return
            for j in range(i,len(nums)):
                if val + nums[j] > target:
                    break
                ds.append(nums[j])
                dfs(j,ds,val + nums[j])
                ds.pop()

        dfs(0,[],0)
        return res