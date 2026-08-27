class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def getNeighbors(x, y):
            neighbors = []
            
            if 0 <= x + 1 < len(grid):
                neighbors.append((x+1, y))
            if 0 <= x - 1 < len(grid):
                neighbors.append((x-1, y))
            if 0 <= y + 1 < len(grid[x]):
                neighbors.append((x, y+1))
            if 0 <= y - 1 < len(grid[x]):
                neighbors.append((x, y-1))
            
            return neighbors
            
        h = []
        h.append((grid[0][0],0,0))
        visited = {}

        while h:
            d, x, y = heapq.heappop(h)
            if (x, y) in visited:
                continue
            
            visited[(x, y)] = d

            for x2, y2 in getNeighbors(x, y):
                d2 = max(grid[x2][y2] - visited[(x, y)], 0)
                heapq.heappush(h, (d + d2, x2, y2))
        
        m = len(grid) - 1
        n = len(grid[-1]) - 1
        return visited[(m, n)]
            



