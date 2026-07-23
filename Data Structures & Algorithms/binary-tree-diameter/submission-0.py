# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        def dfs(node):
            nonlocal res
            longest_l = 1 + dfs(node.left) if node.left else 0
            longest_r = 1 + dfs(node.right) if node.right else 0

            longest_path = longest_l + longest_r
            res = max(res, longest_path)
            return max(longest_l, longest_r)
        
        dfs(root)
        return res
            
            
        