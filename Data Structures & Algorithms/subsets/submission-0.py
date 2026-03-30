class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            if i>=len(nums):
                res.append(sub[:])
                return
            sub.append(nums[i])
            dfs(i+1)
            
            sub.pop()
            dfs(i+1)

        res=[]
        sub=[]
        dfs(0)
        return res