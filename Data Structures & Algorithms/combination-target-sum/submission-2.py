class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, ds, total):
            if target == total:
                res.append(ds.copy())
                return 
            if i >= len(nums) or total > target:
                return
            ds.append(nums[i])
            dfs(i,ds,total + nums[i])
            ds.pop()
            dfs(i+1,ds,total)

        dfs(0,[],0)
        return res