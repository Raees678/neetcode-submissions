# hierholzer's algorithm
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        
        tickets.sort(reverse=True)
        for s, d in tickets:
            g[s].append(d)

        path = []

        def dfs(source):
            while g[source]:
                # we can revisit nodes but never edges
                # when you use an edge i.e. a path between source and dest pop it
                # so that it can never be used again
                dest = g[source].pop()
                dfs(dest)

            path.append(source)
            return
        
        dfs("JFK")
        path.reverse()
        return path