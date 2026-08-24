from typing import List

class Twitter:

    def __init__(self):
        self.twitter = []
        self.follow_list = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twitter.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []

        following = self.follow_list.get(userId, set())

        for author, tweetId in reversed(self.twitter):
            
            if author == userId or author in following:
                result.append(tweetId)

            if len(result) == 10:
                break

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_list:
            self.follow_list[followerId] = set()

        self.follow_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_list:
            self.follow_list[followerId].discard(followeeId)