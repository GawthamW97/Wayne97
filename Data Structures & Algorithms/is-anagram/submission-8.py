from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq1 = Counter(s)
        freq2 = Counter(t)

        if freq1 == freq2:
            return True
        return False