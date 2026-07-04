class Solution:
    def myPow(self, x: float, n: int) -> float:
        temp=x
        


        for i in range(abs(n)-1):
            temp=temp*x
            print(temp)
        if n<0:
            return (1/temp)
        elif n==0:
            return float(1)
        else:
            return(temp)