class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        count=Counter(s1)
        print(count)
        l=0
        for i in range(1,len(s2)+1):
            print(Counter(s2[l:i]))
            if Counter(s2[l:i])==count:
                return True 
            if len(s2[l:i])>=len(s1):
                print("yes")
                l+=1
        return False
        
