# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root.val == targetSum:
            if not root.right and not root.left:
                return True
            elif not root.right:
                return self.countSum(root.left, targetSum, root.val)
            elif not root.left:
                return self.countSum(root.right, targetSum, root.val)
            else:
                return self.countSum(root.right, targetSum, root.val) or self.countSum(root.left, targetSum, root.val)
        return self.countSum(root, targetSum, 0)
    def countSum(self, root, targetSum, count):
        if not root:
            return False
        count += root.val
        if not root.left and not root.right:
            return targetSum == count

        return self.countSum(root.right, targetSum, count) or self.countSum(root.left, targetSum, count)
        