# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        dummy = ListNode(0, head)
        leftPrev = dummy
        prev = head
        cur = head.next
        found_similar = False

        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
                found_similar = True
            else:
                if found_similar:
                    leftPrev.next = cur
                    prev = prev.next
                else:
                    leftPrev = prev
                    prev = prev.next
                found_similar = False

            cur = cur.next

        if found_similar == True and cur == None:
            leftPrev.next = None
            leftPrev = None
            
        return dummy.next