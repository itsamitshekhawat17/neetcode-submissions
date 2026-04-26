import heapq
from typing import List
class Twitter:

    def __init__(self):
        self.time = 0
        self.userTweet = {}
        self.follows={}


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userTweet:
            self.userTweet[userId] = []
        self.userTweet[userId].append((self.time , tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        #make sure user follow himself
        if userId not in self.follows:
            self.follows[userId] = set()
        self.follows[userId].add(userId)

        for user in self.follows[userId]:
            if user in self.userTweet and self.userTweet[user]:
                index = len(self.userTweet[user])-1
                time , tweetId = self.userTweet[user][index]
                heapq.heappush(heap,(-time,tweetId,user,index))
        while heap and len(res) < 10:
            time, tweetId, user, index = heapq.heappop(heap)
            res.append(tweetId)

            if index > 0:
                next_time, next_tweet = self.userTweet[user][index - 1]
                heapq.heappush(heap, (-next_time, next_tweet, user, index - 1))

        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            if followeeId in self.follows[followerId] and followeeId!=followerId:
                self.follows[followerId].remove(followeeId)

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)