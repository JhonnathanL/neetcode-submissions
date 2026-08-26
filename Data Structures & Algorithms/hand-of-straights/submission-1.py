from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        while count:
            start = min(count)

            for i in range(groupSize):
                if count.get(start + i, 0) == 0:
                    return False

                count[start + i] -= 1

                if count[start + i] == 0:
                    del count[start + i]

        return True