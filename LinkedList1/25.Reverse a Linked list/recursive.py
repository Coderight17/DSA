# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(temp, prev):
            if temp is None:
                return prev
            next7 = temp.next
            temp.next = prev
            prev = temp
            return reverse(next7, temp )
        temp = head
        prev = None
        return reverse(head, None)
#Runtime -> 0 ms Beats 100%
#Memory -> 19.09 MB Beats 5.48%
