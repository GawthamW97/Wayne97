class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l,r = 0,0
        ans = []
        while l < len(temperatures):
            while r < len(temperatures) - 1 and temperatures[r] <= temperatures[l]:
                r += 1
            print(temperatures[r], temperatures[l])
            if temperatures[r] <= temperatures[l]:
                ans.append(0)
            else:
                ans.append(r-l)
            l += 1
            r = l
        return ans
