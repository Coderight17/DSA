# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h1 = ListNode(-1)
        h2 =  ListNode(-1)
        h1 = head
        h2 = head
        while h1 != None and h2 != None and h2.next != None:
            h1 = h1.next
            h2 = h2.next.next
            if h1 == h2:
                return True

'''
Runtime
61
ms
Beats
5.55%

Memory
19.89
MB
Beats
56.46%

'''
