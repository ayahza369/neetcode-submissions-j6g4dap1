class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st=''
        for n in digits:
            st+=str(n)
        st=int(st)
        st+=1
        arr=[]
        while st:
            
            arr.append(st%10)
            st=st//10
        arr.reverse()
        return(arr)