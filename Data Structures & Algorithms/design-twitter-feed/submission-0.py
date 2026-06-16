import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.countMax = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.countMax,tweetId])
        self.countMax -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # ordered starting from recent
        minHeap = []
        self.followers[userId].add(userId)
        for followeeId in self.followers[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                minHeap.append([count,tweetId,followeeId,index - 1])
            
        heapq.heapify(minHeap)
            
        while minHeap and len(res) < 10:
            count,tweetId,followeeId,index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count,tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap,[count,tweetId,followeeId,index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
