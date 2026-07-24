# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # does node p contain subtree starting at node q
        def same(p, q):                      # q shrinks. compare only.
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return (p.val == q.val
                    and same(p.left, q.left)
                    and same(p.right, q.right))

        def search(p):                       # q is always subRoot. search only.
            if p is None:
                return False
            return same(p, subRoot) or search(p.left) or search(p.right)

        return search(root)
            
