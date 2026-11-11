# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        left = 0
        right = len(ans) - 1
        while left < right:
            if ans[left] != ans[right]:
                return False
            left += 1
            right -= 1
        return True