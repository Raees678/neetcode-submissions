from functools import cache

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(list)

        for s, d, price in flights:
            g[s].append((price, d))
        
        @cache
        def dfs(node, k):
            nonlocal dst
            
            if k < 0:
                return float("inf")
            
            if node == dst:
                return 0

            price = float("inf")
            for edge_price, neighbor in g[node]:
                neighbor_price = edge_price + dfs(neighbor, k - 1)
                price = min(price, neighbor_price)
            
            return price
        
        res = dfs(src, k + 1)
        return -1 if res == float("inf") else res