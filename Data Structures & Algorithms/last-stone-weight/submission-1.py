import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        miniHeap = [-i for i in stones]
        heapq.heapify(miniHeap)
        while miniHeap and len(miniHeap) > 1:
            x = heapq.heappop(miniHeap)
            y = heapq.heappop(miniHeap)
            if x != y:
                heapq.heappush(miniHeap,x - y)
        if miniHeap:
            return miniHeap[0] * -1
        return 0