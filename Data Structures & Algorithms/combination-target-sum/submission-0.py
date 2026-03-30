class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
       res=[]
       def dfs(i,cur,counter):
            if (counter==target):
                res.append(cur[:])
                return
            if i>=len(nums) or counter>target:
                return
            cur.append(nums[i])
            dfs(i,cur,counter+nums[i])
            cur.pop()
            dfs(i+1,cur,counter)
       dfs(0,[],0)
       return res