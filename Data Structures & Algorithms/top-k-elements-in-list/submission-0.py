from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        bagList = [[]] * (len(nums) + 1)
        
        for key,v in freq.items():
            bagList[v] = bagList[v]+ [key]
        returnList = []

        for i in range(len(bagList) - 1, -1, -1):
            if len(bagList[i]) > 0 and len(returnList) < k:
                returnList += bagList[i]
        
        return returnList

