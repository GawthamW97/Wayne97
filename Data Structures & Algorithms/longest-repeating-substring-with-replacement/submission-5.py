class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        counter = {}
        maxSize = 0
        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r],0) + 1
            if ((r-l+1) - max(counter.values())) > k:
                counter[s[l]] -= 1
                l+=1
            maxSize = max(maxSize, r - l + 1)
        return maxSize
            