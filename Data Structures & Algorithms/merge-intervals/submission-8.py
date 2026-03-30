class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return []
        elif len(intervals)==1:
            return intervals
        else:
            intervals.sort(key=lambda x:x[0])
            other=[intervals[0]]
            
            print(intervals)
            for i in range(1,len(intervals)):
                before=other[-1]
                current=intervals[i]
                if current[0]<=before[1]:
                    before[1]=max(before[1],current[1])
                else:
                    other.append(current)
            return other
                    
