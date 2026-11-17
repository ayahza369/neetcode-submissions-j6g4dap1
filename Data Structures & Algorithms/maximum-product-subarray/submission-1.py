class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_min=[nums[0]]
        dp_max=[nums[0]]
        for i in range(1,len(nums)):
            dp_max.append(max(dp_max[i-1]*nums[i],nums[i],nums[i]*dp_min[i-1]))
            dp_min.append(min(dp_max[i-1]*nums[i],nums[i],nums[i]*dp_min[i-1]))
        return(max(dp_max))
        