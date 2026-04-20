# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        if head is None:
            return None
        curr = head 
        front = head
        prev = None
        while curr:
            front = curr.next 
            curr.next = prev
            prev = curr
            curr = front
        return prev
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None
        slow = head
        fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next 
        slow.next = None
        head_r = self.reverse(second)
        p1 = head
        p2 = head_r
        while p1 and p2:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2 
            p2.next = temp1
            p1 = temp1
            p2 = temp2
        


        
        
        