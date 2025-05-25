# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hA = ListNode(-1)
        hB = ListNode(-1)
        s = set()
        hA = headA
        hB = headB
        while hA != None:
            s.add(hA)
            hA = hA.next
        while hB != None:
            if hB in s:
                return hB
            hB = hB.next

      '''
      Runtime 82ms beats 73.16% 
      Memory 28.51MB beats 7.63%
      '''
