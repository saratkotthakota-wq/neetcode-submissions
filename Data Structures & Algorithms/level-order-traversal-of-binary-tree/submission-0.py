# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        out = []
        queue = [root]
        while len(queue) > 0:
            temp = []
            for _ in range(len(queue)):
                head = queue.pop(0)
                temp.append(head.val)
                if head.left:
                    queue.append(head.left)
                if head.right:
                    queue.append(head.right)
            out.append(temp)
        return out

            

        