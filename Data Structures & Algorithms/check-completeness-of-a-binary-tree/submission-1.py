from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        seen = False
        while queue:
            node = queue.popleft()
            if not node:
                seen = True
            else:
                if seen:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True

        
        