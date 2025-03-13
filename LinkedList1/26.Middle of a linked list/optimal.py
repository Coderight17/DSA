# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise = head
        hare = head
        while hare is not None and hare.next is not None and tortoise is not None:
            tortoise = tortoise.next
            hare = hare.next.next
        return tortoise
#All test cases passed
#Runtime : 0ms, beats 100%
#Memory 17.88MB, beats 30.92%
