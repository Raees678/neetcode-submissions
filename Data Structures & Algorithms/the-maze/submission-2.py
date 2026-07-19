import collections
from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows = len(maze)
        cols = len(maze[0])
        start = tuple(start)
        destination = tuple(destination)
        
        # Use a Set to track visited STOPPING points (not every cell passed)
        visited = set()
        visited.add(start)
        
        # BFS Queue
        queue = collections.deque([start])
        
        # Directions: (row_delta, col_delta)
        # These correspond to Down, Up, Right, Left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            curr_r, curr_c = queue.popleft()
            
            # If we popped the destination, we found a path where the ball STOPS there
            if (curr_r, curr_c) == destination:
                return True
            
            for dr, dc in directions:
                new_r, new_c = curr_r, curr_c
                
                # --- THE OPTIMIZATION ---
                # Keep rolling in the current direction until we hit a wall or edge.
                # We do this in a tight loop instead of recursion.
                while 0 <= new_r + dr < rows and \
                      0 <= new_c + dc < cols and \
                      maze[new_r + dr][new_c + dc] == 0:
                    
                    new_r += dr
                    new_c += dc
                
                # 'new_r, new_c' is now the position BEFORE the wall (the stopping point)
                
                if (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c))
        
        return False