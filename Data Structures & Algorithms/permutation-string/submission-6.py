class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        subStr = [0] * 26
        window = [0] * 26

        for char in s1:
            subStr[ord(char) - ord("a")] += 1
        
        l = 0
        for r in range(len(s2)):
            if (r - l + 1) > len(s1):
                window[ord(s2[l]) - ord("a")] -= 1
                l += 1
            window[ord(s2[r]) - ord("a")] += 1
            
            if window == subStr:
                return True
        
        return False