class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_fruits = 0
        q = deque()
        visited = set()
        max_time = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh_fruits += 1
                elif grid[i][j] == 2:
                    q.append((i,j,0))
                    visited.add((i,j))
        
        def add(i, j, time):
            nonlocal max_time, fresh_fruits
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and (i,j) not in visited and grid[i][j] == 1:
                q.append((i, j, time))
                visited.add((i, j))
                fresh_fruits -= 1
                max_time = max(max_time, time)
            return
        

        while len(q):
            i, j, time = q.popleft()
            add(i + 1, j, time + 1)
            add(i - 1, j, time + 1)
            add(i, j + 1, time + 1)
            add(i, j - 1, time + 1)
        
        if fresh_fruits > 0:
            return -1
        else:
            return max_time



        

