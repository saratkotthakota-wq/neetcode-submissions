"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        hashmap = {None: None}
        node = head
        while node != None:
            hashmap[node] = Node(node.val)
            node = node.next
        
        node = head
        while node:
            hashmap[node].next = hashmap[node.next]
            hashmap[node].random = hashmap[node.random]
            node = node.next
        return hashmap[head]


        