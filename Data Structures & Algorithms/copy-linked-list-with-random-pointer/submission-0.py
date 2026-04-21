"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy 
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        temp = head
        while temp:
            copynode = Node(temp.val)
            copynode.next = temp.next
            temp.next = copynode
            temp = temp.next.next
        temp = head
        while temp:
            copynode = temp.next
            if temp.random:
                copynode.random = temp.random.next
            else:
                copynode.random = None
            temp = temp.next.next
        dummy = Node(-1)
        res = dummy
        temp = head
        while temp:
            res.next = temp.next
            temp.next = temp.next.next
            res = res.next
            temp = temp.next
        return dummy.next

       
        