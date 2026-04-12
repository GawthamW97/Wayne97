class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paran = {"(":")","[":"]","{":"}"}
        if len(s) % 2 != 0:
            return False
        
        for i in range(len(s)):
            if i == 0 and s[i] not in paran:
                return False
            if s[i] in paran:
                stack.append(s[i])
                continue
            if len(stack) > 0:
                curr = stack.pop()
                if paran[curr] != s[i]:
                    return False
        return len(stack) == 0