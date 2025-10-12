class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[1]))
        prev = intervals[0]
        count=0
        for i in range(1,len(intervals)):
            start = intervals[i][0]
            if prev[1]>start:
                count+=1
            else:
                prev=intervals[i]
        return count


        