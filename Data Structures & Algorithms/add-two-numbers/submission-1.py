# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr = l1
        l2_curr = l2
        res = res_head = ListNode()
        carry = 0

        while l1_curr or l2_curr or carry:
            l1_digit = l1_curr.val if l1_curr else 0
            l2_digit = l2_curr.val if l2_curr else 0
            carry, digit = divmod(l1_digit + l2_digit + carry, 10)
            res.next = ListNode(digit)
            res = res.next
            l1_curr = l1_curr.next if l1_curr else None
            l2_curr = l2_curr.next if l2_curr else None
        
        return res_head.next