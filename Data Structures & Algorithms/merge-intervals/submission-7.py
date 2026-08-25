class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                temp = [res[-1][0], max(res[-1][1], end)]
                res.pop()
                res.append(temp)
            else:
                res.append([start,end])
        
        return res
