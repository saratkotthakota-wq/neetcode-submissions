# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge2Lists(self, l1, l2):
        head = ListNode(-1000000000, None)
        dummy = head
        while l1 and l2:
            l1val, l2val, l1next, l2next = l1.val, l2.val, l1.next, l2.next
            if l1val <= l2val:
                dummy.next = l1
                dummy.next.next = None
                l1 = l1next
            else:
                dummy.next = l2
                dummy.next.next = None
                l2 = l2next
            dummy = dummy.next
        if l1:
            dummy.next = l1
        else:
            dummy.next = l2
        return head.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    merged.append(self.merge2Lists(lists[i], lists[i+1]))
                else:
                    merged.append(lists[i])
            lists = merged
        return lists[-1]
