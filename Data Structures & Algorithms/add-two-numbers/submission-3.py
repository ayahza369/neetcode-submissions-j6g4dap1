# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        final=ListNode()
        dummy=final
        remainder=0
        while l1 or l2:

            if l1 and l2:
                n1=l1.val
                n2=l2.val
                l1=l1.next
                l2=l2.next
                
            elif l1:
                
                n1=l1.val
                l1=l1.next
                n2=0
            elif l2:
                
                
                n2=l2.val
                l2=l2.next
                
                n1=0
            total=n1+n2+remainder
            if total>=10:
                remainder=1

                final.next=ListNode((total%10))

                
            else:
                remainder=0
                final.next=ListNode(total)
            final=final.next
        if remainder>0:
            final.next=ListNode(remainder)
            final=final.next
        return dummy.next
