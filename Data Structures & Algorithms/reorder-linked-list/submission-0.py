# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        rhalf = self.reverseList(slow.next)
        slow.next = None

        start = head
        while rhalf:
            tmp1, tmp2 = start.next, rhalf.next
            start.next = rhalf
            rhalf.next = tmp1
            start, rhalf = tmp1, tmp2
        