"""
Problem: Design Twitter
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Example 1:
Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]
"""
import collections
import heapq

class Twitter:
    def __init__(self):
        # We use a global count to simulate timestamps.
        # Negative count makes Python's Min-Heap act like a Max-Heap (most recent first).
        self.count = 0
        # Map each user to a list of their tweets [count, tweetId].
        self.tweetMap = collections.defaultdict(list)
        # Map each user to a set of people they follow.
        self.followMap = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        # Decrement count so the next tweet has a "smaller" timestamp (higher priority in Min-Heap).
        self.count -= 1

    def getNewsFeed(self, userId: int):
        res = []
        minHeap = []
        
        # A user always implicitly follows themselves to comfortably see their own tweets.
        self.followMap[userId].add(userId)
        
        # Collect the single most recent tweet from EVERY person this user follows.
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # Get the last index (most recent tweet) in their list.
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                # Push [timestamp, tweetId, who_posted_it, previous_tweet_index].
                minHeap.append([count, tweetId, followeeId, index - 1])
                
        # Turn our list into a valid Heap.
        heapq.heapify(minHeap)
        
        # Pull up to 10 most recent tweets from the Heap.
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            # If the user who posted this tweet has MORE older tweets, add the next one to the Heap!
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

if __name__ == "__main__":
    obj = Twitter()
    obj.postTweet(1, 5)
    print(f"getNewsFeed(1): {obj.getNewsFeed(1)}")
    obj.follow(1, 2)
    obj.postTweet(2, 6)
    print(f"getNewsFeed(1): {obj.getNewsFeed(1)}")
    obj.unfollow(1, 2)
    print(f"getNewsFeed(1): {obj.getNewsFeed(1)}")
