# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        traversed = {}
        temp = ListNode()
        temp = head

        while temp:
            if temp in traversed:
                return True
            traversed[temp] = True
            temp = temp.next

        return False