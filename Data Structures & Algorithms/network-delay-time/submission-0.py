class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(set)
        for s, d, time in times:
            g[s].add((time, d))

        times = {}
        
        h = [(0, k)]
        while h:
            time, node = heapq.heappop(h)
            # if youve seen node before you've surely seen a lower time
            # since we pop based on the lowest time
            if node not in times:
                times[node] = time
                
                for t, d in g[node]:
                    # the time it takes to reach a neighbor is the time it took
                    # to reach me + the time it takes to travel the edge
                    heapq.heappush(h, (time + t, d))
        
        if len(times) == n:
            return max(times.values())
        else:
            return -1


