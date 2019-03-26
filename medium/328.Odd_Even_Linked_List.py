# 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        evenHead = head.next
        oddTail = head
        evenTail = head.next
        while evenTail and evenTail.next:
            oddTail.next = oddTail.next.next
            evenTail.next = evenTail.next.next
            oddTail = oddTail.next
            evenTail = evenTail.next
        
        oddTail.next = evenHead
        
        return head
