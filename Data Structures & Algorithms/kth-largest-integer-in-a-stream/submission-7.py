import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        temp=[]
        for n in nums[:k]:
            temp+=[n]
        heapq.heapify(temp)
        if len(nums)>k:
            for n in nums[k:]:
                heapq.heappushpop(temp,n)

        
        self.nums=temp
        print(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums)==self.k:
            heapq.heappushpop(self.nums,val)
        else:
            heapq.heappush(self.nums,val)
        print(self.nums)
        new=self.nums[0]
        
       
        return new
        