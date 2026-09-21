# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}

        def dfs(node):
            if not node:
                return 0

            if node in cache:
                return cache[node]

            val = node.val
            if node.left:
                val += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                val += dfs(node.right.left) + dfs(node.right.right)
            val = max(val, dfs(node.left) + dfs(node.right))
            cache[node] = val
            return val
        return dfs(root)
        