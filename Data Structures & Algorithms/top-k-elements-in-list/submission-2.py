import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for (el, c) in count.items():
            heapq.heappush(heap, (c, el))
            if len(heap) > k:
                heapq.heappop(heap)
        
        largest = heapq.nlargest(k, heap)
        return [i[1] for i in largest]
        