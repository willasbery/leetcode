class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0

        # sort by end point of interval
        intervals.sort(key=lambda x: x[1])
        
        curr_endpoint = intervals[0][1]
        for i in range(1, len(intervals)): # skip first interval since it's already counted
            if curr_endpoint > intervals[i][0]: # if the intervals overlap
                res += 1
            else:
                curr_endpoint = intervals[i][1] # update the current endpoint

        return res