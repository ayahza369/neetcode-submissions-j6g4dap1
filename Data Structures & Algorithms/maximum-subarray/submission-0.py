class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalSum=-100000
        maxSum=-1000000
        for i in range(len(nums)):
            maxSum=max(nums[i],nums[i]+maxSum)
            if maxSum>globalSum:
                globalSum=maxSum
        return globalSum    


