# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=head
        counter=0
        while dummy: 
            counter+=1
            dummy=dummy.next
        step=counter-n
        
        curr=head
        if counter==1 and n>0:
            return ListNode('')
       

        for i in range(abs(step-1)):
            print(curr.next)
            curr=curr.next
            print(curr.val)
        
        if not curr.next or step==0:
            head=curr
        else:
            curr.next=curr.next.next
        return head
