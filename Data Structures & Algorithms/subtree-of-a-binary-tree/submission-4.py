# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # does node p contain subtree starting at node q
        # this needs to be 2 functions because p and q each move differently
        # when comparing if one tree is part of another
        # think of dfs like a loop
        # outer loop loops over start positions p
        # inner loop loops over all vales of q

        # loops over all values q, moving both p and q
        # and checking if they are equal
        def same(p, q): # q shrinks. compare only.
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            return (p.val == q.val
                    and same(p.left, q.left)
                    and same(p.right, q.right))

        # loops over all start pos p
        # checks if it can match all q to this p position
        # and then moves on to future values of p
        def search(p): # q is always subRoot. search only.
            if p is None:
                return False
            return same(p, subRoot) or search(p.left) or search(p.right)

        return search(root)
            
