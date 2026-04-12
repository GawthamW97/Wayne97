class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paran = {")":"(","]":"[","}":"{"}
        
        for char in s:
            if char in paran: 
                if stack and stack[-1] == paran[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0