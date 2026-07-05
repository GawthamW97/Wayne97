from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT = Counter(t)
        window = {} # current window count 
        have  = 0 # number of character currently meet the required count
        need = len(countT) # how many distinct character we need to match
        res = [-1,-1]
        resLen = float("infinity")

        l = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1

            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l: r + 1] if resLen != float("infinity") else ""

            

        