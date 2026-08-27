class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals, key=lambda x: x[0])

        prev = intervals[0][1]
        removes = 0

        for start, end in intervals[1:]:
            if start < prev:
                removes += 1
                prev = min(end, prev)
            
            else:
                prev = end

        return removes