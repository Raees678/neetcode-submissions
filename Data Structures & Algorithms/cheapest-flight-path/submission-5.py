# Djikstras
# normally in dijkstras we store the min distance to a given node and dont update
# once we find it
# but here we need to store the min distance for a given number of steps
# then finally at the end we query the min distance for dst
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(list)
        for s, d, price in flights:
            g[s].append((price, d))

        h = []
        h.append((0, 0, src))
        d = {}

        while h:
            price, stops, node = heapq.heappop(h)            
            if (node, stops) in d or stops > k + 1:
                continue
            
            if node == dst:
                return price
            
            d[(node, stops)] = price
            
            for edge_price, neighbor in g[node]:
                heapq.heappush(h, (price + edge_price, stops + 1, neighbor))

        return -1
            

            


