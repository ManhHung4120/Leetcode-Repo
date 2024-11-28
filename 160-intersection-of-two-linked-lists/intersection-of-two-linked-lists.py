# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        if headA is headB:
            return headA
        headC = headA
        headD = headB
        lastA = headA
        lastB = headB
        countA = 0
        countB = 0
        while headC:
            countA += 1
            if headC.next == None:
                lastA = headC
                break
            headC = headC.next
        while headD:
            countB += 1
            if headD.next == None:
                lastB = headD
                break
            headD = headD.next
        if lastA is not lastB:
            return None
        if countA > countB:
            for i in range(0, countA - countB):
                headA = headA.next
            while headA:
                headC = headB
                while headC:
                    if headC is headA:
                        return headA
                    headC = headC.next
                headB = headB.next
                headA = headA.next
        else:
            for i in range(0, countB - countA):
                headB = headB.next
            while headB:
                headC = headA
                while headC:
                    if headC is headB:
                        return headA
                    headC = headC.next
                headB = headB.next
                headA = headA.next
        
        return None
        