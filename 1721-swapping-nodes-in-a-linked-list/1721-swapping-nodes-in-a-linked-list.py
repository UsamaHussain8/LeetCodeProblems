# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        length = i = 0
        j = 1
        while i < k - 1:
            i += 1
            cur = cur.next

        leftNode = rightNode = cur
        length = k
        cur = head

        while rightNode.next:
            rightNode = rightNode.next
            length += 1
        while j <= length - k:
            cur = cur.next
            j += 1

        leftNode.val, cur.val = cur.val, leftNode.val

        return head
        