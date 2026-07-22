# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next = head

        prev = sentinel
        curr = head
        stack = []
        while curr:
            if len(stack) == k:
                while len(stack) > 0:
                    node = stack.pop()
                    prev.next = node
                    prev = node
            
            stack.append(curr)
            curr = curr.next
        
        if len(stack) == k:
            while len(stack) > 0:
                node = stack.pop()
                prev.next = node
                prev = node
        
        prev.next = stack[0] if len(stack) > 0 else None
        return sentinel.next
