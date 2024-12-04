# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        second = ListNode()
        new_head = second
        while head:
            if head.val != val:
                second.next = head
                second = second.next
            else:
                second.next = None
            head = head.next
        return new_head.next
        