class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target: 
                return mid
            elif nums[mid]<target:
                if nums[right]>=nums[mid] and target<=nums[right]:
                    left=left+1
                else:
                    right=right-1

            else:
                if nums[left]<=nums[mid] and target>=nums[left]:
                    right=right-1
                else:
                    left+=1
        return -1
