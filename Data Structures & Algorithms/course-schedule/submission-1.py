class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        for p in prerequisites:
            indegree[p[0]] += 1
        
        g = defaultdict(list)
        for p in prerequisites:
            g[p[1]].append(p[0])

        q = deque()

        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        
        while len(q):
            c = q.popleft()
            for c2 in g[c]:
                indegree[c2]-=1
                if indegree[c2] == 0:
                    q.append(c2)
  
        return not any(indegree)