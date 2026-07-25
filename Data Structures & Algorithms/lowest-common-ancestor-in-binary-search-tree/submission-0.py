# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs_search(node, target):
            if node is None:
                return []
            if target.val == node.val:
                return [node]
            
            l = dfs_search(node.left, target)
            if len(l):
                l.append(node)
                return l
            
            r = dfs_search(node.right, target)
            if len(r):
                r.append(node)
                return r
            
            return []
            
        
        p_parents = dfs_search(root, p)
        q_parents = dfs_search(root, q)

        i = -1
        limit = -min(len(p_parents), len(q_parents))
        res = None

        while i >= limit:
            if p_parents[i] != q_parents[i]:
                break
            res = p_parents[i]
            i -= 1
        
        return res