# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, min_val, max_val):
            l = not node.left or min_val < node.left.val < node.val
            r = not node.right or max_val > node.right.val > node.val
            return l and r
        
        def dfs(node, min_val, max_val):
            if not node:
                return True
            v = valid(node, min_val, max_val)
            l = dfs(node.left, min_val, node.val)
            r = dfs(node.right, node.val, max_val)
            return v and l and r

        
        return dfs(root, float("-inf"), float("inf"))

            

