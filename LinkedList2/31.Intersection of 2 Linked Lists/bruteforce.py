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
        while hA != None:
            hB = headB
            while hB != None:
                if hA == hB:
                    return hB
                hB = hB.next
            hA = hA.next
        return None

  '''
Time Limit Exceeded
35 / 39 testcases passed
  '''
