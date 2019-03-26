# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        prev = self
        prev.next = head
        dummy = prev
        curr = head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:  
                prev = prev.next
            curr = curr.next
            
        return dummy.next
