# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def dfs(node):
            nonlocal res
            if not node:
                return 0

            v = node.val

            l = dfs(node.left)
            r = dfs(node.right)

            s = max(v, v + l, v + r, v + l + r)
            res = max(res, s)

            return max(v, v + l, v + r)
        
        dfs(root)
        return res


