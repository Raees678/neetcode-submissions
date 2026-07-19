"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr is not None:
            newNode = Node(curr.val, curr.next, curr.random)
            curr.next = newNode
            curr = curr.next.next
        
        curr = head
        i = 0
        while curr is not None:
            if i % 2 == 1:
                curr.random = curr.random.next if curr.random else None
            i += 1
            curr = curr.next
        
        curr = head
        newHead = newCurr = Node(0)
        while curr is not None:
            newCurr.next = curr.next
            newCurr = newCurr.next
            curr.next = curr.next.next
            curr = curr.next
            
        
        return newHead.next
        

