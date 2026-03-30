class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet=set(nums)
        maximum=0
        for element in mySet:
            
            if element-1 not in mySet:
                length=0
                num=element
                while (num+length) in mySet:
                    
                    length+=1
                maximum=max(maximum,length)
                
        return maximum
            
                
            

