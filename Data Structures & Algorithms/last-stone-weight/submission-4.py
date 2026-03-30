class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        if len(stones)==1:
            return stones[0]
        for stone in stones:
            heap.append(-stone)
        heapq.heapify(heap)
        while len(heap)>1:
            first=heapq.heappop(heap)
            second=heapq.heappop(heap)
            if first!=second:
                heapq.heappush(heap,(first-second))
            print(heap)
        if not heap:
            return 0
        return -heap[0]
