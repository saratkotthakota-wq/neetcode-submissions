# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        out = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                out.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                out.append("N")
        return ",".join(out)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N":
            return None
        root = TreeNode(int(vals[0]))
        queue = [root]

        idx = 1
        while queue:
            node = queue.pop(0)
            if vals[idx] != "N":
                node.left = TreeNode(int(vals[idx]))
                queue.append(node.left)
            idx += 1
            if vals[idx] != "N":
                node.right = TreeNode(int(vals[idx]))
                queue.append(node.right)
            idx += 1
        return root


