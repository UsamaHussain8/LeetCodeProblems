# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = head
        prev = dummy
        list_len = 0

        while cur:
            cur = cur.next
            list_len += 1
        
        mid_ind = list_len // 2
        cur_ind = 0
        cur = head

        while cur_ind <= mid_ind - 1:
            cur = cur.next
            prev = prev.next
            cur_ind += 1
  
        prev.next = cur.next

        return dummy.next