# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    paths = []

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root.left and not root.right:
            return [str(root.val)]
        self.paths = []
        self.travelTree(root, "")
        return self.paths

    def travelTree(self, root, path):
        path += str(root.val)

        if root.left and root.right:
            self.travelTree(root.left, path + "->")
            self.travelTree(root.right, path + "->") 
        elif root.left:        
            self.travelTree(root.left, path + "->")
        elif root.right:
            self.travelTree(root.right, path + "->")
        else:
            self.paths.append(path)

        return path
