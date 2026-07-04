class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        
        intervals=sorted(intervals, key=lambda x:x[0])
        print(intervals)
        final=[intervals[0]]
        prevEnd=intervals[0][1]
        for interval in intervals[1:]:
            if interval[0]<=final[-1][1]:
                prevEnd=max(prevEnd,interval[1])
                final[-1][1]=prevEnd
            else:
                final.append(interval)
            
            print(final)
        return(final)
