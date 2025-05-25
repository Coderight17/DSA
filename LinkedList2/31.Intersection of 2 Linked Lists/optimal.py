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
        while hA != hB:
            if hA == None:
                hA = headB
            else:
                hA = hA.next
            if hB == None:
                hB = headA
            else:
                hB = hB.next
        return hA

  '''
  Runtime
88
ms
Beats
40.97%

Memory
27.88
MB
Beats
43.03%
  '''
