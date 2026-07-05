class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            print(nums[mid])
            if (nums[mid-1]>=nums[mid] and mid==len(nums)-1) or (nums[mid+1]>=nums[mid] and mid==0) or (nums[mid-1]>=nums[mid] and nums[mid]<=nums[mid+1]):
                return nums[mid]
            else: 
                if nums[mid]<=nums[r]:
                    r=mid-1
                    print('y')
                else:
                    l=mid+1
                    print('y')
            
            
            print(nums[mid])
        return nums[0]
