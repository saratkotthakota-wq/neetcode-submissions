# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy, count = head, 1
        while dummy.next:
            dummy = dummy.next
            count += 1
        place = count - n
        if place == 0:
            return head.next
        dummy = head
        for i in range(count-1):
            if i+1 == place:
                dummy.next = dummy.next.next
                break
            dummy = dummy.next
        return head




        