# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr = l1
        l2_curr = l2
        carry_over = 0
        res_head = res = ListNode()

        while l1_curr and l2_curr:
            val = l1_curr.val + l2_curr.val + carry_over
            carry_over = val // 10
            res.next = ListNode(val % 10)
            res = res.next
            l1_curr = l1_curr.next
            l2_curr = l2_curr.next
        
        while l1_curr:
            val = l1_curr.val + carry_over
            carry_over = val // 10
            res.next = ListNode(val % 10)
            res = res.next
            l1_curr = l1_curr.next
        
        while l2_curr:
            val = l2_curr.val + carry_over
            carry_over = val // 10
            res.next = ListNode(val % 10)
            res = res.next
            l2_curr = l2_curr.next
        
        if carry_over > 0:
            res.next = ListNode(carry_over)
        
        return res_head.next

