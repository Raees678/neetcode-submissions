class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        g = defaultdict(list)
        e = {}
        
        for i, (s, d) in enumerate(edges):
            g[s].append(d)
            g[d].append(s)
            e[(s,d)] = i
        
        visited = set()
        path = []
        cycle_start_found = False
        def dfs(node, parent):
            nonlocal cycle_start_found
            if node in visited:
                return True
            
            visited.add(node)
            for c in g[node]:
                if c != parent:
                    found = dfs(c, node)
                    if found:
                        if not cycle_start_found:
                            path.append((node, c))
                        if node == path[0][1]:
                            cycle_start_found = True
                        return True

            return False

        dfs(1, None)
        
        res_val = float("-inf")
        res = None
        for edge in path:
            if edge not in e:
                edge = (edge[1], edge[0])
            if e[edge] > res_val:
                res = edge
                res_val = e[edge]

        return [res[0], res[1]]


            

