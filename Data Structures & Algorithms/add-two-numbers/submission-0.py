# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 , temp2 = l1,l2
        carry = 0
        curr_sum = 0 
        dummy = ListNode(-1)
        res = dummy
        while temp1 or temp2:
            curr_sum = carry
            if temp1:
                curr_sum+=temp1.val 
                temp1 = temp1.next
            if temp2:
                curr_sum+=temp2.val 
                temp2 = temp2.next
            carry = curr_sum//10
            curr_sum = curr_sum%10
            res.next = ListNode(curr_sum)
            res = res.next
        if carry == 1:
            res.next = ListNode(1)
        return dummy.next

            
       


