from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = defaultdict(list)
        for word in strs:
            subList = [0] * 26
            for c in word:
                subList[ord("a") - ord(c)] += 1
            hMap[tuple(subList)].append(word)
        
        return [v for k,v in hMap.items()]

