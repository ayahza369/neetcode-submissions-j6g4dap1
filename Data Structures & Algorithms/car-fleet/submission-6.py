class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        myDict={}
        times=[]
        for i in range(len(position)):
            myDict[position[i]]=speed[i]
        print(myDict)
        myDict=dict(sorted(myDict.items(), reverse=True))
       
        for key,val in myDict.items():
            time=(target-key)/val
            if times:
                temp=times[-1]
                if temp>=time:
                    pass
                else:
                    times.append(time)
                    
            else:
                times.append(time)
            
        return(len(times))

        
                