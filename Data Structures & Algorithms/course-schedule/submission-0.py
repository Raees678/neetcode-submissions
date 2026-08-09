class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g_in = defaultdict(set)
        g_out = defaultdict(set)
        taken = set()
        n = numCourses
        for course, prereq in prerequisites:
            g_out[prereq].add(course)
            g_in[course].add(prereq)

        def dfs(course):
            nonlocal n
            if course in taken:
                return
            if not g_in[course].issubset(taken):
                return
            
            taken.add(course)
            n -= 1
            for next_course in g_out[course]:
                dfs(next_course)
            return

        while True:
            old_n = n
            for course in range(numCourses):
                if course not in taken:
                    dfs(course)
            if n == old_n:
                break
        
        return n == 0

        


        