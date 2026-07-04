class Solution:
    def isHappy(self, n: int) -> bool:
        notSeen=True
        seen=set()
        total=0
        while notSeen:
            while n:
                total+=(n%10)**2
                n=n//10
                print(n)
            if total==1:
                return True 
            elif total in seen:
                notSeen=False
                return False
            seen.add(total)
            n=total
            total=0
        return False