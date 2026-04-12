class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paran = {")":"(","]":"[","}":"{"}
        if len(s) % 2 != 0:
            return False
        
        for i in range(len(s)):
            if s[i] in paran and len(stack) > 0:
                if i == 0:
                    return False
                curr = stack.pop()
                if paran[s[i]] != curr:
                    return False
            else:
                stack.append(s[i])
        return len(stack) == 0