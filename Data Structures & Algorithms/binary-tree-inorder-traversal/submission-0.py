# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []

        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                out.append(node.val)
                return
            if node.left:
                dfs(node.left)
            out.append(node.val)
            if node.right:
                dfs(node.right)


        dfs(root)
        return out

        