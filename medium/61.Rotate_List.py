# 61. Rotate List
# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        end = head
        _len = 1
        while end.next:
            end = end.next
            _len += 1
        ptr = head
        end.next = head
        for i in range(_len-k%_len-1):
            ptr = ptr.next
        
        head = ptr.next
        ptr.next = None
        
        return head
