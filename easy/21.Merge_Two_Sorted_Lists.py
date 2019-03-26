# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        ptr1, ptr2 = l1, l2
        
        dummy = ListNode(-1)
        result = dummy
        
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                temp = ptr1.next
                result.next = ptr1
                result = result.next
                ptr1 = temp
            else:
                temp = ptr2.next
                result.next = ptr2
                result = result.next
                ptr2 = temp
        
        if ptr1:
            result.next = ptr1
        elif ptr2:
            result.next = ptr2
            
        return dummy.next
        
