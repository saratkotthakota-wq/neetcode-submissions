# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []

        def dfs(node):
            if node is None:
                return -1
            curr = max(dfs(node.left), dfs(node.right))+1
            if len(out) == curr:
                out.append([])
            out[curr].append(node.val)
            return curr
        dfs(root)
        return out
        
        