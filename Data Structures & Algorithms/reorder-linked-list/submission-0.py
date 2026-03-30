# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev, curr = None, slow.next
        slow.next=None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        first=head
        second=prev
        while second:
            old=first.next
            after=second.next
            first.next=second
            second.next=old
            first=old
            second=after

        print(slow)
