# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        if p.val != q.val:
            return False
        p_tree = self.travelTree(p, [])
        q_tree = self.travelTree(q, [])
        if p_tree == q_tree:
            return True
        return False
    def travelTree(self, node, result = []):
        if node is None:
            result.append("")
            return result

        if node:
            result.append(node.val)
            self.travelTree(node.left, result)
            self.travelTree(node.right, result)

        return result

        