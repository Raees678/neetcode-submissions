# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        d = {}
        curr = head
        i = 0
        while curr is not None:
            d[i] = curr
            i += 1
            curr = curr.next
        
        i -= 1
        
        l = 0
        r = i

        while l < r - 1:
            d[r-1].next = d[r].next
            d[r].next = d[l].next
            d[l].next = d[r]
            l += 1
            r -= 1        
        