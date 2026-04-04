class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        total = 0
        for char in s:
            if char not in t:
                return False
                
        for i in range(len(s)):
            total ^= ord(s[i]) ^ ord(t[i])

        if total > 0:
            return False

        return True