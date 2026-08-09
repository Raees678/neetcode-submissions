class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        q = deque()
        visited = set()
        topleft = set()
        bottomright = set()

        def add(i, j, h):
            if (
                0 <= i < len(heights) and
                0 <= j < len(heights[i]) and
                (i, j) not in visited and
                heights[i][j] >= h
            ):
                    q.append((i, j))
                    visited.add((i, j))
            return


        for i in range(len(heights[0])):
            q.append((0, i))
            visited.add((0, i))
        for i in range(len(heights)):
            if (i, 0) not in visited:
                q.append((i, 0))
                visited.add((i, 0))
        
        while len(q):
            i, j = q.popleft()
            topleft.add((i, j))
            h = heights[i][j]
            add(i+1, j, h)
            add(i-1, j, h)
            add(i, j+1, h)
            add(i, j-1, h)

        visited = set()
        r = len(heights) - 1
        c = len(heights[r]) - 1
        for i in range(len(heights[-1])):
            q.append((r, i))
            visited.add((r, i))
        for i in range(len(heights)):
            if (i, c) not in visited:
                q.append((i, c))
                visited.add((i, c))
        
        while len(q):
            i, j = q.popleft()
            bottomright.add((i, j))
            h = heights[i][j]
            add(i+1, j, h)
            add(i-1, j, h)
            add(i, j+1, h)
            add(i, j-1, h)
        
        res =  []
        for (i, j) in topleft.intersection(bottomright):
            res.append([i, j])
        
        return res





        
        