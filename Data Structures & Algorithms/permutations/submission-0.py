class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recurse(ds,idx):
            if idx == len(ds):
                res.append(ds.copy())
                return
            
            for i in range(idx,len(ds)):
                ds[idx],ds[i] = ds[i],ds[idx]
                recurse(ds,idx+1)
                ds[idx],ds[i] = ds[i],ds[idx]

        recurse(nums,0)
        return res