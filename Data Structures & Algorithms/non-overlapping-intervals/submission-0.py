class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        count = 0
        intervals.sort(key=lambda x:x[0])

        prevEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            if prevEnd <= intervals[i][0]:
                prevEnd = intervals[i][1]
            else:
                count += 1
                prevEnd = min(prevEnd, intervals[i][1])
        return count
        