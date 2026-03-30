class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        alist = set()
        blist=[]
        nums.sort()
        
        for i in range(len(nums)-2):
            
            r,l= i+1,len(nums)-1
            
            while r<l:
                if nums[i]+nums[r]+nums[l]>0:
                    l-=1
                elif nums[i]+nums[r]+nums[l]<0:
                    r+=1
                    
                elif nums[i]+nums[r]+nums[l]==0:
                    alist.add((nums[i],nums[r],nums[l]))
                    r+=1
                    l-=1
            print(alist)
        for obj in alist:
            print(obj)
            a,b,c = obj
            blist.append([a,b,c])
        return blist

