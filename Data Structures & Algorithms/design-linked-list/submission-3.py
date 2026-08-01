class Node:
    def __init__(self,val,nxt,prev):
        self.val=val
        self.nxt=nxt
        self.prev=prev

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.length=0

    
        

    def get(self, index: int) -> int:
        if index>=0:
            dummy=self.head
            count=0
            while dummy:
                
                if count==index:
                    return dummy.val
                dummy=dummy.nxt
                count+=1
                 
                    
        return -1


    def addAtHead(self, val: int) -> None:
        if self.head:
            dummy=self.head
        
            added=Node(val,None,None)
            
            added.nxt=dummy
            dummy.prev=added
        
            
            self.head=added
        else:
            self.head=Node(val,None,None)
        self.length+=1

        

    def addAtTail(self, val: int) -> None:
        if self.head:
            dummy=self.head
       
            while dummy.nxt:
                dummy=dummy.nxt
            added=Node(val,None,None)
            
            dummy.nxt=added
            
            added.prev=dummy
      
        else:
            self.head=Node(val,None,None)
        self.length+=1
    def addAtIndex(self, index: int, val: int) -> None:
        if self.length==index:
            self.addAtTail(val)
        elif index<self.length:
            if self.head:
                dummy=self.head
                count=0
                while dummy:
                    if count==index-1:
                        added=Node(val,None,None)
                        temp=dummy.nxt
                        dummy.nxt=added
                        added.prev=dummy
                        added.nxt=temp
                        temp.prev=added
                    count+=1
                    dummy=dummy.nxt
                self.length+=1
            else:
                pass

    def deleteAtIndex(self, index: int) -> None:
        if index>=0 and self.head:
            dummy=self.head
            count=0
            while dummy:
                if count==index:
                    if dummy.prev and dummy.nxt:
                        new=dummy.prev
                        new.nxt=dummy.nxt
                        dummy.nxt.prev=new
                        print(dummy.nxt.prev.val,new.val)
                    elif dummy.prev:
                        
                        new=dummy.prev
                        new.nxt=None
                        dummy.prev=None
                    elif dummy.nxt:
                        self.head=dummy.nxt
                        dummy.nxt.prev=self.head
                    self.length-=1
                    break
                count+=1
                dummy=dummy.nxt



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)