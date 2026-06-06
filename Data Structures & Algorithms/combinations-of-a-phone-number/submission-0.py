class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        dic = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        def dfs(i,c):
            if i == len(digits):
                res.append(c)
                return
            
            for j in dic[digits[i]]:
                dfs(i+1, c + j)
        
        if digits:
            dfs(0,"")

        return res

