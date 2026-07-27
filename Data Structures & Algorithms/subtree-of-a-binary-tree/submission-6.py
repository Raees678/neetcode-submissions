# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # inner loop that compares two trees
        def compare(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val \
                and compare(p.left, q.left) \
                and compare(p.right, q.right)

        # outer loop that iterates over all in tree comparing each
        # tree to its subtree
        def dfs(p):
            if not p:
                return not subRoot
            
            return compare(p, subRoot) \
                or dfs(p.left) \
                or dfs(p.right)

        return dfs(root)
