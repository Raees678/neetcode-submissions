# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_d = { el:idx for idx, el in enumerate(inorder) }
        
        def dfs(pre_l, pre_r, in_l, in_r):
            root = preorder[pre_l]
            root_idx = inorder_d[root]

            # these are guaranteed to be 0 or more
            # if we ensure that in_l and in_r are the 
            # beginning and end of the inorder list of
            # the subtree that contains root
            l_len = root_idx - in_l
            r_len = in_r - root_idx

            node = TreeNode(root)

            # now we gotta make sure that when recurse
            # we pass through the correct indices for the relevant
            # left and right subtrees. this works because:
            # subtrees of preorder and inorder traversals
            # will also be preorder and inorder themselves
            # and as long we ensure that the arrays correspond to 
            # the correct subtrees we will never exceed indices
            if l_len:
                node.left = dfs(pre_l + 1, 
                                pre_l + l_len,
                                in_l,
                                root_idx - 1)

            if r_len:
                node.right = dfs(pre_l + l_len + 1, 
                                pre_l + l_len + r_len,
                                root_idx + 1,
                                in_r)

            return node
        
        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)


            



