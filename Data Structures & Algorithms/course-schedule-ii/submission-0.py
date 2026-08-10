class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        g = defaultdict(list)
        for c, p in prerequisites:
            g[p].append(c)
            indegree[c] += 1
        
        q = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        
        res = []
        while len(q):
            c = q.popleft()
            res.append(c)
            for n in g[c]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        
        if any(indegree):
            return []
        return res
            
