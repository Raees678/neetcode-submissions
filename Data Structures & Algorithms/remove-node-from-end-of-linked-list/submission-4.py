# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if you have a single element to remove then remove it
        # and return None
        if not head.next:
            return None

        i = j = 0
        iprev = None
        inode = head
        jnode = head
        while jnode:
            if j - i >= n:
                i += 1
                iprev = inode
                inode = inode.next

            j += 1
            jnode = jnode.next
        
        # at this point iprev points to the node before the one
        if iprev:
            iprev.next = inode.next
            return head
        else:
            return inode.next
        