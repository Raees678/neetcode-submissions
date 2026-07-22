# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            temp = node.left
            node.left = node.right
            node.right = temp
        
        def recurse(node):
            if node:
                invert(node)
                if node.left:
                    recurse(node.left)
                if node.right:
                    recurse(node.right)
            return
        
        recurse(root)
        return root

        