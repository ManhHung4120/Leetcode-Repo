# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not len(nums):
            return None
        middle_index = math.floor(len(nums)/2)
        print(middle_index)
        left = [nums[i] for i in range (0, middle_index)]
        right = [nums[j] for j in range (middle_index + 1, len(nums))]

        root = TreeNode(nums[middle_index])
        if len(left):
            root.left = self.sortedArrayToBST(left)
        if len(right):
            root.right = self.sortedArrayToBST(right)
        print(root)
        return root
        