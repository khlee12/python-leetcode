# 21.Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        result = ListNode(-1)
        end_pointer = result
        
        while l1 or l2:
            l1_val = l1.val if l1 else None
            l2_val = l2.val if l2 else None
            
            if not l1_val is None and ((not l2_val is None and l1_val <= l2_val) or l2_val is None):
                
                temp_node = ListNode(l1_val)
                l1 = l1.next if l1 else None
            else:
                if not l2_val is None and ((not l1_val is None and l1_val > l2_val) or l1_val is None):
                    temp_node = ListNode(l2_val)
                    l2 = l2.next if l2 else None
            end_pointer.next = temp_node
            end_pointer = end_pointer.next
            
        return result.next   
