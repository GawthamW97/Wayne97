class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        i = 0

        def dfs(i,ds):
            if i == len(nums):
                res.append(ds.copy())
                return
            ds.append(nums[i])
            dfs(i+1,ds)
            ds.pop()
            dfs(i+1,ds)
        
        dfs(0,[])
        return res
        