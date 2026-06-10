from math import sqrt
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        minHeap = []
        for point in points:
            distance = sqrt(point[0]*point[0] + point[1]*point[1])
            heapq.heappush(minHeap,[distance,point])

        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res
            
