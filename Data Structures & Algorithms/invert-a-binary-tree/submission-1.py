# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        elif root.left == None and root.right == None:
            return root
        else:
            rightcpy = root.right
            leftcpy = root.left
            root.left = self.invertTree(rightcpy)
            root.right = self.invertTree(leftcpy)
            return root
        