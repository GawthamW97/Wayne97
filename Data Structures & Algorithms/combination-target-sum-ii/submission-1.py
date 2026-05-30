class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        def dfs(i,ds,total):
            if total == target:
                res.append(ds.copy())
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if total + candidates[j] > target:
                    break
                ds.append(candidates[j])
                dfs(j+1,ds,total + candidates[j])
                ds.pop()
        dfs(0,[],0)
        return res
                
                