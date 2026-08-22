from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown = deque()
        
        count = Counter(tasks)
        heap = [(-c, t) for t, c in count.items()]
        heapq.heapify(heap)

        t = 0
        while len(heap) or len(cooldown):
            if len(heap):
                cnt, task = heapq.heappop(heap)
                cnt += 1
                if cnt < 0:
                    cooldown.append((t + n, cnt, task))

            if len(cooldown) and cooldown[0][0] == t:
                _, cnt, task = cooldown.popleft()
                heapq.heappush(heap, (cnt, task))

            t += 1

        return t