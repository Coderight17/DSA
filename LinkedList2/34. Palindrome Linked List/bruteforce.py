# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverselinkedlist(head):
            l7 = ListNode(-1)
            l8 = ListNode(-1)
            l9 = ListNode(-1)
            l8 = head
            l9 = head.next
            while l9 is not None  :
                if l8 == head:
                    l8.next = None
                else:
                    l8.next = l7
                l7 =l8
                l8 = l9
                l9 = l9.next
                l8.next = l7
            return l8
        if head is None:
            return False
        if head.next is None:
            return True
        l7 = ListNode(-1)
        l8 = ListNode(-1)
        l7 = head
        cnt = 0
        while l7 != None:
            l7 = l7.next
            cnt = cnt + 1
        l7 = head
        for i in range(cnt//2):
            l7 = l7.next
        l8 = reverselinkedlist(l7.next)
        l9 = l8
        if cnt%2 == 0:
            reverselinkedlist(l7)
        else:
            reverselinkedlist(l7.next)
        l7 = head
        while l7 != l9 and l8 != None:
            if l7.val != l8.val:
                return False
            l7 = l7.next
            l8 = l8.next
        return True
  '''
  Runtime
37
ms
Beats
45.18%

Memory
39.37
MB
Beats
36.05%
'''
