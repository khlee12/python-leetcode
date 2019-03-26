# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        prev = head
        curr = head
        while curr:
            
            if curr.val != prev.val:
                prev.next = curr
                prev = curr
            
            curr = curr.next
        prev.next = None  
        return head
                
