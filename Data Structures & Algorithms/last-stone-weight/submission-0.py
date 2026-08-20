import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)
        while len(stones) >= 2:
            s1 = -heapq.heappop(stones)
            s2 = -heapq.heappop(stones)

            if s1 > s2:
                diff = s1 - s2
                s1 = diff
                heapq.heappush(stones, -s1)
        
        if len(stones):
            return -stones[0]
        else:
            return 0

