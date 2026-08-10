class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for s, d in edges:
            g[s].append(d)
            g[d].append(s)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return
            
            visited.add(node)
            for child in g[node]:
                if child != parent:
                    dfs(child, node)
            
            return

        res = 0
        for node in range(n):
            if node not in visited:
                dfs(node, None)
                res += 1
        
        return res

