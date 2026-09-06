# 1,2,2,3,3,4

# 1,1,
# 2,2,2,
# 3,3,3,
# 4,4

from collections import Counter
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        count = Counter(hand)
        heap = hand.copy()
        heapq.heapify(heap)

        # pick min element with non zero count
        while heap:
            min_element = heapq.heappop(heap)
            if count[min_element] == 0:
                continue
            
            # try to form a group
            i = 0
            while i < groupSize:
                if min_element + i not in count or count[min_element + i] == 0:
                    return False
                else:
                    count[min_element + i] -= 1
                i += 1
        
        return True


                





