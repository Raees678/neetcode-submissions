import heapq

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.timestamp = 0
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        # go through the user's tweets
        for timestampedTweet in self.tweets[userId]:
            heapq.heappush(heap, timestampedTweet)
            if len(heap) > 10:
                heapq.heappop(heap)

        # go through all the user's following tweets
        for following in self.following[userId]:
            for timestampedTweet in self.tweets[following]:
                heapq.heappush(heap, timestampedTweet)
                if len(heap) > 10:
                    heapq.heappop(heap)
        
        res = []
        while heap:
            timestamp, tweet = heapq.heappop(heap)
            res.append(tweet)
        
        res.reverse()
        self.timestamp += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        self.timestamp += 1
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        self.timestamp += 1
        
