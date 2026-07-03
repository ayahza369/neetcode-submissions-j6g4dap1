class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        arr=sorted(intervals, key=lambda x:x[0])
        print(arr)
        prevEnd=arr[0][1]
        count=0
        l=1
        for i in range(1,len(arr)):
            
            if arr[i][0]>=prevEnd:
                prevEnd=arr[i][1]
            else:
                prevEnd=min(prevEnd,arr[i][1])
                count+=1
                
            l+=1
        return(count)
            
