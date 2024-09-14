# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        list_elements: List[int] = []
        cur = head

        while cur != None:
            list_elements.append(cur.val)
            cur = cur.next

        cur = head
        reversedList = ListNode()
        i: int = len(list_elements) - 1
        while cur != None:
            cur.val = list_elements[i]
            i -= 1
            cur = cur.next
        
        return head
