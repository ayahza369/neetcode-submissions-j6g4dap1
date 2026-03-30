class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp_f=[0]*len(nums)
        dp_l=[0]*len(nums)
        dp_f[0]=nums[0]
        
        dp_f[1]=max(dp_f[0],nums[1])
        dp_l[1]=nums[1]
        for i in range(2,len(nums)):
            
            dp_l[i]=max(dp_l[i-1],dp_l[i-2]+nums[i])
        for i in range(2,len(nums)-1):
            dp_f[i]=max(dp_f[i-1],dp_f[i-2]+nums[i])
        return max(max(dp_l),max(dp_f))
            