# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ptr = dummy
        while list1 or list2:
            if not list1:
                ptr.next = list2
                break
            if not list2:
                ptr.next = list1
                break
            v1, v2 = list1.val, list2.val
            if v1 < v2:
                ptr.next = ListNode(v1)
                list1 = list1.next
                ptr = ptr.next
            else:
                ptr.next = ListNode(v2)
                list2 = list2.next
                ptr = ptr.next
        return dummy.next

        