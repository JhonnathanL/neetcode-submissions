class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            stones.sort()

            if stones[-2] == stones[-1]:
                stones.pop()
                stones.pop()

            else:
                stones[-1] -= stones[-2]
                stones.pop(-2)

        return stones[0] if stones else 0

            
            
                

