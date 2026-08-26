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
                dest = g[source].pop()
                dfs(dest)

            path.append(source)
            return
        
        dfs("JFK")
        path.reverse()
        return path