class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        while stones:
            if len(stones) == 1:
                return stones[0]
            
            stones.sort()
            print(stones)
            if stones[-2] == stones[-1]:
                stones.pop()
                stones.pop()
            
            elif stones[-2] < stones[-1]:
                stones[-1] -= stones[-2]
                stones.pop(len(stones) - 2)  
            
            if len(stones) == 0:
                return 0

            
            
                

