from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        heap = hand.copy()
        heapq.heapify(heap)

        # pick min element with non zero count
        while heap:
            min_element = heapq.heappop(heap)
            if count[min_element] == 0:
                continue
            
            # try to form a group
            for i in range(min_element, min_element + groupSize):
                if count[i] == 0:
                    return False
                else:
                    count[i] -= 1
        
        return True


                





