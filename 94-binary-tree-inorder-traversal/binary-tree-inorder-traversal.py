# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree = self.travelNode(root, [])
        return tree
    
    def travelNode(self, root, result = []):
        if root:
            self.travelNode(root.left, result)
            result.append(root.val)
            self.travelNode(root.right, result)
        return result

        