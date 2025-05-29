# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fg = 0
        if head == None or head.next == None or head.next.next == None:
            return None
        # if head.next.next == head:
        #     return head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fg = 1
                break
        if fg == 0:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
'''
Runtime
42
ms
Beats
82.26%

Memory
19.61
MB
Beats
54.09%

'''
