class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()

        def valid(i, j):
            if (
                0 <= i < len(grid) and 
                0 <= j < len(grid[i]) and 
                (i,j) not in visited and
                grid[i][j] > 0
            ):
                return True
            return False
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
                    visited.add((i, j))

        
        while len(q):
            i, j, dist = q.popleft()
            grid[i][j] = dist
            if valid(i+1, j):
                q.append((i+1, j, dist+1))
                visited.add((i+1,j))
            if valid(i-1, j):
                q.append((i-1, j, dist+1))
                visited.add((i-1,j))
            if valid(i, j+1):
                q.append((i, j+1, dist+1))
                visited.add((i,j+1))
            if valid(i, j-1):
                q.append((i, j-1, dist+1))
                visited.add((i,j-1))
        
        return





