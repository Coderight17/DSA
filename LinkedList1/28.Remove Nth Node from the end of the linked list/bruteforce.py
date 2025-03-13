# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        cnt = 0
        while temp is not None:
            temp = temp.next
            cnt = cnt + 1
        c = 0
        if cnt == n:
            newhead = head.next
            head = None
            return newhead
        prev = None
        temp = head
        while c < cnt-n:
            prev = temp
            temp = temp.next
            c = c+1
        if temp is not None and prev is not None:
            prev.next = temp.next
        else:
            return None
        return head
#All test cases passed
#Runtime 0ms beats 100%
#Memory 17.70MB beats 84.78%
