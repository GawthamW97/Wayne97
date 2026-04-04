from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq1 = Counter(s)
        freq2 = Counter(t)

        for i in range(len(s)):
            if not freq2[s[i]] or freq1[s[i]] != freq2[s[i]]:
                return False
        return True