# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        cur = ListNode(-1)
        start = ListNode(-1)
        prev = ListNode(-1)
        start = cur
        while l1 is not None and l2 is not None:
            s = l1.val + l2.val + carry
            carry = s//10
            value = s % 10
            cur.val = value
            prev = cur
            cur.next  = ListNode(-1)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            s = l1.val  + carry
            carry = s//10
            value = s % 10
            cur.val = value
            prev = cur
            cur.next  = ListNode(-1)
            cur = cur.next
            l1 = l1.next
        while l2 is not None:
            s = l2.val  + carry
            carry = s//10
            value = s % 10
            cur.val = value
            prev = cur
            cur.next  = ListNode(-1)
            cur = cur.next
            l2 = l2.next
        if carry != 0:
            cur.val = carry
        else:
            prev.next = None
            print('Carry is zero')
        return start
# Runtime
# 7
# ms
# Beats
# 32.19%
# Analyze Complexity
# Memory
# 17.85
# MB
# Beats
# 57.58%
