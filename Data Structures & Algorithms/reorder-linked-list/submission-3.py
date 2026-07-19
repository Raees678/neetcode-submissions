# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [0,1,2] -> [0, *2*, 1]
# [0,1,2,3] -> [0, *3*, 1, 2]
# [0,1,2,3,4] -> [0, *4*, 1, *3*, 2]
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 0 or 1 elem lists are already in order
        if not head or not head.next:
            return

        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is guaranteed to be the middle or later middle element
        # since we took care of 0 and 1 elem lists
        
        # reverse the list from slow.next till the end
        curr = slow.next
        revhead = ListNode()
        while curr:
            next = curr.next
            curr.next = revhead.next
            revhead.next = curr
            curr = next

        # decouple slow from its next list
        slow.next = None

        # merge the head and revhead.next
        l = head
        r = revhead.next
        while l and r:
            lnext = l.next
            rnext = r.next
            r.next = l.next
            l.next = r
            l = lnext
            r = rnext
        
        return



        
        



        

            
            