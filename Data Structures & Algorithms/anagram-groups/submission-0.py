from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            counter = [0] * 26 #a to z

            for c in s:
                counter[ord(c) - ord("a")] += 1

            res[tuple(counter)].append(s)

        return list(res.values())