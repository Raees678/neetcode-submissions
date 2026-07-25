# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            nonlocal k
            if not node:
                return -1
            l = dfs(node.left)
            if l != -1:
                return l

            k -= 1
            if k == 0:
                return node.val

            return dfs(node.right)
        
        return dfs(root)
        
        