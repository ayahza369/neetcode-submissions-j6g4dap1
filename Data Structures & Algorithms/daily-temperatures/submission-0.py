class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        myStack=[]
        answer=[0]*len(temperatures)
        for i in range(len(temperatures)):
            
           
            while myStack and temperatures[myStack[-1]]<temperatures[i]:
                num=myStack.pop()
                answer[num]=i-num
            myStack.append(i)
        return (answer)
            