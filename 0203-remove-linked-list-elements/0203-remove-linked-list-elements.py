# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head

        dummy = ListNode(0, None)
        prev = dummy
        cur = head

        while cur:
            curNext = cur.next
            if head.val == val:
                head = curNext
            elif cur.val == val:
                prev.next = curNext
            else:        
                prev = cur
            cur = curNext

        return head