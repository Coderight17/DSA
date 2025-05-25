# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hA = ListNode(-1)
        hB = ListNode(-1)
        hA = headA
        hB = headB
        c7 = 0
        c8 = 0
        diff = 0
        while hA != None:
            c7 = c7 + 1
            hA = hA.next
        while hB != None:
            c8 = c8+1
            hB = hB.next
        if c7 > c8:
            diff = c7 - c8
            hA = headA
            hB = headB
            for i in range(diff):
                hA = hA.next
        else:
            diff = c8 - c7
            hA = headA
            hB = headB
            for i in range(diff):
                hB = hB.next
        while hA != None and hB != None:
            if hA == hB:
                return hA
            hA = hA.next
            hB = hB.next
        return None

'''
Runtime
100
ms
Beats
5.53%

Memory
27.72
MB
Beats
69.19%

'''
