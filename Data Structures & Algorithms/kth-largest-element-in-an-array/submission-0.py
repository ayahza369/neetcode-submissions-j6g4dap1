class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        myList=[]
        for i in range(len(nums)):
            myList.append(-nums[i])
        heapq.heapify(myList)

        while k>0:
            num=heapq.heappop(myList)
            k-=1
        return(-num)