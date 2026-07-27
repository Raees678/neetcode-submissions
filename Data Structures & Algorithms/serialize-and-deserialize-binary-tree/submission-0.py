# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("null")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        print(res)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            if i >= len(nodes) or nodes[i] == "null":
                return None
            
            node = TreeNode(int(nodes[i]))
            i += 1
            node.left = dfs()
            i += 1
            node.right = dfs()
            return node
        
        return dfs()

            


