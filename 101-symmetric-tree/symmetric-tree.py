# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        

        left_branch = self.travelBranch(root.left,"left", [])
        right_branch = self.travelBranch(root.right, "right", [])

        if left_branch != right_branch:
            return False
        return True
    def travelBranch(self, node, side, result = []):
        if node is None:
            result.append("")
            return result
        if side == "right":
            result.append(node.val)
            self.travelBranch(node.right, "right", result)
            self.travelBranch(node.left, "right", result)
        else:
            result.append(node.val)
            self.travelBranch(node.left, "left", result)
            self.travelBranch(node.right, "left", result)
        
        return result

        
        