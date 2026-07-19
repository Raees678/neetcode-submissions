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

        # now you are guaranteed that removing a node will leave 1 node in the list
        # so you must always be returning a valid Node
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
        # you want to remove (could be None if you remove the head)
        
        # if its not None then you just remove iprev's next node and return the head
        if iprev:
            iprev.next = inode.next
            return head
        else:
            # if you remove the head iprev is None and you must return the new head
            return inode.next
        