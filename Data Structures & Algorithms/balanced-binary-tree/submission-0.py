# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
            
        stop = False
        res = True
        def dfs(node):
            nonlocal stop, res
            lheight = 1 + dfs(node.left) if node.left else 0
            rheight = 1 + dfs(node.right) if node.right else 0

            if abs(lheight - rheight) > 1:
                stop = True
                res = False

            return max(lheight, rheight)
        
        dfs(root)
        return res


        