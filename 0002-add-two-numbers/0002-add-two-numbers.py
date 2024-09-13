# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number_l1: int = 0
        number_l2: int = 0
        exp: int = 0

        cur_l1: ListNode = l1
        cur_l2: ListNode = l2

        while cur_l1 or cur_l2:
            if cur_l1:
                number_l1 += cur_l1.val * (10 ** exp)
                cur_l1 = cur_l1.next
            if cur_l2:
                number_l2 += cur_l2.val * (10 ** exp)
                cur_l2 = cur_l2.next
            
            exp += 1
        
        res = number_l1 + number_l2
        digits = [int(digit) for digit in str(res)]
        
        head = None
        for value in digits:
            newNode = ListNode(value)
            newNode.next = head
            head = newNode

        return head