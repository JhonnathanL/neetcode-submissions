class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            curr_start = res[-1][0]
            curr_end = res[-1][1]

            if start <= curr_end:
                temp = [curr_start, max(end, curr_end)]
                res.pop()
                res.append(temp)
            else:
                res.append([start,end])
        
        return res



        