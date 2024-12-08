# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        heigh = self.countHeigh(root)
        heigh_right = self.countHeighRight(root)
        if heigh == heigh_right:
            return pow(2, heigh) - 1
        
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def countHeigh(self, root):
        if not root:
            return 0
        return 1 + self.countHeigh(root.left)
    def countHeighRight(self,root):
        if not root:
            return 0
        return 1 + self.countHeighRight(root.right)
            

        