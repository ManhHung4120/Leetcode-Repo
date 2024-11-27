# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = self.travel(root, [])
        return result

    def travel(self, root, result):
        if not root:
            return result
        self.travel(root.left,result)
        self.travel(root.right, result)
        result.append(root.val)
        return result
        