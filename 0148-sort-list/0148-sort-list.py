# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        arr.sort()
        cur = head
        i = 0
        while cur:
            cur.val = arr[i]
            i += 1
            cur = cur.next
        return head
       
        