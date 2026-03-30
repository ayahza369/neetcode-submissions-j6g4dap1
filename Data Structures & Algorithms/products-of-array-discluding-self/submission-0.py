class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mymap=defaultdict(int)
        tri=[]
        for i in range(len(nums)):
            pro=1
            for j in range(len(nums)):
                if i!=j:
                    pro*=nums[j]
            tri+=[pro]
        return tri
