class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum=max(piles)
      
        
        
        l,r=1,maximum
        num=float('inf')
        
        
        while l<=r:
            mid=(l+r)//2
            
            total=0
            for i in range(len(piles)):
                total+=math.ceil(piles[i]/mid)
            print('total:' + str(total))
            if total<=h:
                num=min(num,mid)
                r=mid-1
            else:
                l=mid+1
            
        return(num)
        
