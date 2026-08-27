class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:        
        h = []
        h.append((0, points[0][0], points[0][1]))
        
        res = 0
        visited = set()
        while h:
            d, x, y = heapq.heappop(h)
            if (x,y) not in visited:
                res += d
                visited.add((x, y))
                for x2, y2 in points:
                    if (x2, y2) in visited:
                        continue
                    d2 = abs(x - x2) + abs(y - y2)
                    heapq.heappush(h, (d2, x2, y2))

        return res