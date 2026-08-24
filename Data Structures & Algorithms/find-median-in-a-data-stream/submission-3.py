import heapq

class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.n = 0

    def addNum(self, num: int) -> None:
        # add to the correct heap, choosing to put it in maxheap 
        # if theres nothing there (i.e. both heaps are empty) or
        if len(self.maxheap) == 0 or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)

        # rebalance
        # allow maxheap to have up to 1 el more
        if len(self.maxheap) - len(self.minheap) > 1:
            el = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -el)

        if len(self.minheap) > len(self.maxheap):
            el = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -el)
        
        self.n += 1

    def findMedian(self) -> float:
        if self.n % 2:
            return -self.maxheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0]) / 2