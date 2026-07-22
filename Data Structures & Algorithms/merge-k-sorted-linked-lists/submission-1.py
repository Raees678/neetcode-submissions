# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l, r):
            mergedhead = mergedcurr = ListNode()
            lhead = lcurr = lists[l]
            rhead = rcurr = lists[r]
            
            while lcurr and rcurr:
                if lcurr.val < rcurr.val:
                    mergedcurr.next = lcurr
                    lcurr = lcurr.next
                else:
                    mergedcurr.next = rcurr
                    rcurr = rcurr.next
                # you forgot this
                mergedcurr = mergedcurr.next
                
            if lcurr:
                mergedcurr.next = lcurr
            elif rcurr:
                mergedcurr.next = rcurr
            
            lists[l] = mergedhead.next

        if not lists or not any(lists):
            return None
        
        l = 0
        size = len(lists)
        r = size - 1
        # this runs O(log(k)) times for k lists
        while l < r:
            # merging all these nodes takes O(N) time
            while l < r:
                merge(l, r)
                l += 1
                r -= 1

            l = 0
            # you forgot this
            size = math.ceil(size / 2)
            r = size - 1
        
        return lists[0]