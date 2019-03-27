# 147. Insertion Sort List
# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        ptr = head.next
        end = head
        dummy = ListNode(-1)
        dummy.next = head
        
        while ptr:
            temp = ptr.next
            if ptr.val < end.val:
                curr = dummy.next
                prev = dummy
                while curr and curr.val < ptr.val:
                    curr = curr.next
                    prev = prev.next
                prev.next,ptr.next,end.next = ptr,curr,ptr.next
            else:
                end = end.next
            ptr = temp
        
        return dummy.next
                
                
