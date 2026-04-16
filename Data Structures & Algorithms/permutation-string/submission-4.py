from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2 = len(s1), len(s2)
        window = [0] * 26
        need = [0] * 26

        for char in s1:
            need[ord(char) - ord("a")] +=1
        
        for char in s2[:n1]:
            window[ord(char) - ord("a")] +=1
        
        if window == need:
            return True
        
        for r in range(n1,n2):
            window[ord(s2[r]) - ord("a")] +=1
            window[ord(s2[r - n1]) - ord("a")] -=1
            if window == need:
                return True
        return False
         
                
