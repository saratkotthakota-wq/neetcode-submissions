# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        out = ""
        
        def dfs(root):
            nonlocal out
            if not root:
                out += "N,"
            else:
                out += str(root.val)+","
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        print(out)
        return out
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        i = 0

        def dfs():
            nonlocal i 
            node = None
            if vals[i] == "N":
                i += 1
                return node
            else:
                node = TreeNode(int(vals[i]))
                i += 1
                node.left = dfs()
                node.right = dfs()
            return node
        return dfs()

