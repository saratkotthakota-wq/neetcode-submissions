# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        hashmap = {}
        for i, val in enumerate(inorder):
            hashmap[val] = i
        left = 0
        right = len(inorder) - 1
        pre_idx = 0
        
        def build(left, right):
            nonlocal pre_idx
            if left > right:
                return None
            val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(val)
            root.left = build(left, hashmap[val] - 1)
            root.right = build(hashmap[val] + 1, right)
            return root
        return build(left, right)