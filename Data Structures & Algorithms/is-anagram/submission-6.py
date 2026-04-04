from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        total = 0
        freq = Counter(s)

        for i in range(len(s)):
            if not freq[t[i]]:
                return False
            total ^= ord(s[i]) ^ ord(t[i])

        if total > 0:
            return False

        return True