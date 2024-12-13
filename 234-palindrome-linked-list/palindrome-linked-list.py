# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: 
            return False
        list_val = []
        root = head
        while root:
            list_val.append(root.val)
            root = root.next
        if list_val == list(reversed(list_val)):
            return True
        return False

        