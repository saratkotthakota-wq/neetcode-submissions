# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = [k]
        res = [root.val]

        def dfs(node, cnt, res):
            if not node:
                return

            dfs(node.left, cnt, res)
            cnt[0] -= 1
            if cnt[0] == 0:
                res[0] = node.val
                return
            dfs(node.right, cnt, res)

        dfs(root, cnt, res)
        return res[0]