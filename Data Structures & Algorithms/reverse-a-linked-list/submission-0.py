# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        while head is not None:
            curr = head
            head = head.next
            curr.next = res
            res = curr
        
        return res
