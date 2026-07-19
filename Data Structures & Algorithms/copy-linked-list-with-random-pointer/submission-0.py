"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        myDict={}
        dummy=head
        prev=Node(int('0'))
        dummy2=prev
        while dummy:
            nxt=Node(int(dummy.val))
            myDict[dummy]=nxt
            dummy=dummy.next
            
            
        while head:
            prev.next=myDict[head]
            if head.random in myDict:
                prev.next.random=myDict[head.random]
            else:
                prev.next.random=None
            head=head.next
            prev=prev.next
        return dummy2.next

