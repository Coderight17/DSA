# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp is not None:
            next7 = temp.next
            temp.next = prev
            prev = temp
            temp = next7
        return prev
#All test cases passed
#Runtime 0ms, beats 100%
#Memory 17.99MB, beats 8.60%
