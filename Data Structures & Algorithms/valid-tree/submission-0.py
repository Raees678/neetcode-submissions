class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a tree is a graph where all nodes are strongly connected
        # and there are no cycles

        g = defaultdict(list)
        for n1, n2 in edges:
            g[n1].append(n2)
            g[n2].append(n1)

        visited = set()
        unvisited = n
        
        def dfs(node, parent):
            nonlocal unvisited
            if node in visited:
                return True
            
            visited.add(node)
            unvisited -= 1
            for child in g[node]:
                if child == parent:
                    continue
                cycle = dfs(child, node)
                if cycle:
                    return True
            
            return False
        
        cycle = dfs(0, None)
        if not cycle and unvisited == 0:
            return True
        return False