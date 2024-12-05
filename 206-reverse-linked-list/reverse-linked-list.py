# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current_node = head
        list_val = []
        while current_node:
            list_val.append(current_node.val)
            current_node = current_node.next
        result = ListNode()
        head_node = result
        for i in range(len(list_val) - 1, -1, -1):
            head_node.next = ListNode(list_val[i])
            head_node = head_node.next
        return result.next

        