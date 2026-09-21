/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode[]} lists
     * @return {ListNode}
     */
    merge2Lists(listA: ListNode, listB: ListNode): ListNode {
        let head = new ListNode(-100000000000, null);
        let dummy = head;
        while (listA && listB) {
            let aval = listA.val;
            let bval = listB.val;
            if (aval <= bval) {
                dummy.next = new ListNode(aval, null);
                listA = listA.next;
            } else {
                dummy.next = new ListNode(bval, null);
                listB = listB.next;
            }
            dummy = dummy.next
        }
        if (listA) dummy.next = listA;
        else if (listB) dummy.next = listB;
        return head.next;
    }
    mergeKLists(lists: ListNode[]): ListNode {
        if (!lists || lists.length === 0) {
            return null;
        }
        while (lists.length > 1) {
            let merged = [];
            for (let i = 0; i < lists.length; i+=2) {
                if ((i+1) < lists.length) {
                    let merge = this.merge2Lists(lists[i], lists[i+1]);
                    merged.push(merge)
                } else {
                    merged.push(lists[i])
                }
            }
            lists = merged;
        }
        return lists[0];
    }
}
