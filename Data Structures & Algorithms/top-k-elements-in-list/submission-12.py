from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        freq = defaultdict(set)

        for key,v in counts.items():
            freq[v].add(key)

        res = []
        for count in range(len(nums),0,-1):
            for num in freq[count]:
                res.append(num)

                if len(res) == k:
                    return res