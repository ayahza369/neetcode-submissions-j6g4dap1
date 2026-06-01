class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops=['+','-','/','*']
        nums=[]
        operations=[]
        total=0
        count=0
        
        if len(tokens)==1:
            return int(tokens[0])
        for i in range(len(tokens)):
            if tokens[i] not in ops:
                nums.append(int(tokens[i]))
                
            else:
                op=tokens[i]
                count+=1
                if count==1:
                    n2=nums.pop()
                    n1=nums.pop()
                    print(n1,n2)
                
                else:
                    n2=nums.pop()
                    n1=nums.pop()
                    #n1=nums.pop()
                    #n2=nums.pop()
                
                if op=='+':
                    total=n2+n1
                elif op=='-':
                    total=n1-n2
                elif op=='*':
                    total=n2*n1
                else:
                    if n1==0:
                        total=0
                    else:
                       total=int(n1/n2)
                print(total)
                nums.append(total)
        return nums[0]
                
        
        
