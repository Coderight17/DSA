# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverselinkedlist(head):
            prev = None
            cur = head
            while cur is not None:
                nxt= cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        if head.next is None:
            return True
        slow = head
        fast = head
        while  fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        second_half = reverselinkedlist(slow.next)
        node = head
        while second_half is not None:
            if node.val != second_half.val:
                return False
            node = node.next
            second_half = second_half.next
        return True
