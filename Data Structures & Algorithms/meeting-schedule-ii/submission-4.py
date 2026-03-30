"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start=[]
        end=[]
        if not intervals:
            return 0
        elif len(intervals)==1:
            return 1
        else:
            for interval in intervals:
                start.append(interval.start)
                end.append(interval.end)
            start.sort()
            end.sort()
            l1=0
            l2=0
            count=0
            while l1<len(intervals):
                count+=1
                if start[l1]<end[l2]:
                    l1+=1
                else:
                    count-=1
                    l1+=1
                    l2+=1
            return count