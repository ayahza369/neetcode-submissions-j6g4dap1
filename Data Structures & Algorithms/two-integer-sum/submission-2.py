class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers_set=set()
        numbers_set.add(target-nums[0])
        for i in range(1,len(nums)):
            if nums[i] in numbers_set:
                return [nums.index(target-nums[i]),i]
            difference = target-nums[i]
            numbers_set.add(difference)

            