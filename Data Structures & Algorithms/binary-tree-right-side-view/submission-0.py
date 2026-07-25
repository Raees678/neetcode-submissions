# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        if root:
            q.append((root, 0))
        
        res = []
        while len(q):
            node, lvl = q.popleft()
            if node.left:
                q.append((node.left, lvl+1))
            if node.right:
                q.append((node.right, lvl+1))
            
            if len(res) <= lvl:
                res.append(node.val)
            else:
                res[lvl] = node.val
        
        return res

