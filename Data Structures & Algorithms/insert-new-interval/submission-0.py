class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []

        new_start = newInterval[0]
        new_end = newInterval[1]

        for curr_start, curr_end in intervals:

            if curr_end < new_start:
                result.append([curr_start, curr_end])

            elif curr_start > new_end:
                result.append([new_start, new_end])
                new_start = curr_start
                new_end = curr_end

            else:
                new_start = min(new_start, curr_start)
                new_end = max(new_end, curr_end)

        result.append([new_start, new_end])

        return result