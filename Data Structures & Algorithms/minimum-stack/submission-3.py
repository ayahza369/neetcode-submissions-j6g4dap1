class MinStack:

    def __init__(self):
        self.minstack=[]
        minimum=[]
        heapq.heapify(minimum)
        self.minimum=minimum
        

    def push(self, val: int) -> None:
        self.minstack.append(val)
        self.minimum=list(self.minimum)
        self.minimum.append(val)
        heapq.heapify(self.minimum)
        print(self.minstack)

    def pop(self) -> None:
        
        num=self.minstack.pop()
        self.minimum=list(self.minimum)
        self.minimum.remove(num)
        heapq.heapify(self.minimum)

        

    def top(self) -> int:
        top=self.minstack[-1]
        print(self.minstack)
        return top

    def getMin(self) -> int:
        
        return self.minimum[0]
        
