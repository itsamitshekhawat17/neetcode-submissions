# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        if not head:
            return None
        front = head
        curr = head 
        prev = None
        while curr:
            front = curr.next 
            curr.next = prev
            prev = curr
            curr = front 
        return prev
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_r = self.reverse(head)
        curr = head_r
        prev = None
        t = 1
        while curr:
            if t==n:
                break
            prev = curr
            curr = curr.next
            t+=1
        if prev is None:
            head_r = curr.next
        else:
            prev.next = curr.next
        return self.reverse(head_r)
       


        