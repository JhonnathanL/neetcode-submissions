

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        res = []
        y2, x2 = 0, 0
    
        for x1, y1 in points:
            calculate =  (x1 - x2)**2 + (y1 - y2)**2
            res.append([calculate, [x1, y1]])
        
        res.sort(key=lambda x:x[0])

        return [points for distance, points in res][:k]