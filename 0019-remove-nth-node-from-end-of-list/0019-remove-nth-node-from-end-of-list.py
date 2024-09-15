# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head

        idx: int = 0
        length: int = 1
        cur: ListNode = head
        while cur.next is not None:
            cur = cur.next
            length += 1

        cur = head
        dummy = ListNode(0, head)
        prev = dummy
        while idx != length - n + 1:
            cur_next = cur.next
            cur = cur.next
            idx = idx + 1
            if idx < length - n + 1:
                prev = prev.next

        prev.next = cur

        return dummy.next

