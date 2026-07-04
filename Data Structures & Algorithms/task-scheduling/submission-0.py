class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        print(freq)
        f=[]
        for key, val in freq.items():
            f.append(-val)
        heapq.heapify(f)
        print(f)
        time=0
        line=deque()

        
        while f or line:
            time+=1
            
            if f:
                x=heapq.heappop(f)
                x+=1
                if x<0:
                    line.append([x,time+n])
            if line:
                turn=line[0]
                if turn[1]==time:
                    x=line.popleft()
                    heapq.heappush(f,x[0])
                    
                
        return(time)


        
        

        
