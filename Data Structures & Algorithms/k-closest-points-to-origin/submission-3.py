class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
       
        ans=[]
        heap=[]
        heapq.heapify(heap)
        
        for x,y in points:
            d=math.sqrt(x**2+y**2)
            heapq.heappush(heap,(-d,-x,-y))
            print(heap)
            if len(heap)>k:
                heapq.heappop(heap)
            
        return [[-(num[1]),-(num[2])] for num in heap]
            
        
