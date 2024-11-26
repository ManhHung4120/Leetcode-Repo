# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_travel = head
        slow_travel = head
        while slow_travel and slow_travel.next:
            if not slow_travel.next or not fast_travel.next:
                return False
            
            slow_travel = slow_travel.next
            fast_travel = fast_travel.next
            if not fast_travel.next:
                return False
            fast_travel = fast_travel.next
            if slow_travel.val == fast_travel.val and slow_travel.next == fast_travel.next:
                return True
        return False
        