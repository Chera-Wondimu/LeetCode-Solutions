# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = None
        y = head
        while y:
            next_node = y.next 
            y.next = x        
            x = y             
            y = next_node       
        return x
        