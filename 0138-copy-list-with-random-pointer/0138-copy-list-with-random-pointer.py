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
        oldToCopyMap = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopyMap[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopyMap[cur]
            copy.next = oldToCopyMap[cur.next]
            copy.random = oldToCopyMap[cur.random]
            cur = cur.next

        return oldToCopyMap[head]