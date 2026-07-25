class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def dfs_search(node, target):
            if node is None:
                return []
            if node.val == target.val:
                return [node]
                
            l = dfs_search(node.left, target)
            if l:
                l.append(node)
                return l
            r = dfs_search(node.right, target)
            if r:
                r.append(node)
                return r
            return []

        p_parents = dfs_search(root, p)
        q_parents = dfs_search(root, q)

        i = -1
        limit = -min(len(p_parents), len(q_parents))
        res = None
        while i >= limit:
            print("i", i, p_parents[i].val, q_parents[i].val,
                  p_parents[i] is q_parents[i])
            if p_parents[i] is not q_parents[i]:
                break
            res = p_parents[i]
            i -= 1
        return res