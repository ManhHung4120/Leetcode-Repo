# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = root
        if not head:
            return root
        node_left = None
        node_right = None
        if root.left:
            node_right = self.invertTree(root.left)
        if root.right:
            node_left = self.invertTree(root.right)
        head.left = node_left
        head.right = node_right
        return head
        