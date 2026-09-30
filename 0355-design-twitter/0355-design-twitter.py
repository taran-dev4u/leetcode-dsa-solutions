from collections import defaultdict, deque
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        min_heap = []
        users = self.following[userId] | {userId}
        for user in users:
            if user in self.tweets:
                for time, tweetId in reversed(self.tweets[user]):
                    if len(min_heap) < 10:
                        heapq.heappush(min_heap, (time, tweetId))
                    elif time > min_heap[0][0]:
                        heapq.heappushpop(min_heap, (time, tweetId))
                    else:
                        break
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        return result[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
