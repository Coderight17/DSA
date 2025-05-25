# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h7 = ListNode(-1)
        h7 = head
        s = set()
        while h7 is not None:
            if h7 in s:
                return True
            else:
                s.add(h7)
            h7 = h7.next
        return False

  '''
  Runtime
50
ms
Beats
46.17%

Memory
20.26
MB
Beats
11.33%
  '''
