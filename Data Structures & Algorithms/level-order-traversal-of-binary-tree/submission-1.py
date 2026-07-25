# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# trees cannot skip levels
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        # res will be at most 1 less than our current level since we see levels
        # in order and it starts empty and trees cant skip levels
        res = []
        if root:
            q.append((root, 0))
        while len(q):
            node, level = q.popleft()
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
            
            if len(res) <= level:
                res.append([])
            
            res[level].append(node.val)
        
        return res
            

            

        


                

            