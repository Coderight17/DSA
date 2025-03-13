# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        cnt = 0
        while  cnt < n:
            fast = fast.next
            cnt = cnt+1
        if fast is None:
            return head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        if slow is not None and slow.next is not None:
            slow.next = slow.next.next
        return head
#All test cases passed
#Runtime 0ms beats 100%
#Memory 17.91MB beats 13.03%
