class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []

        for num in range(n+1):
            res.append(bin(num)[2:].count("1"))
        
        return res

