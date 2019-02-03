# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = None
        while head:
            temp = head.next
            head.next = result
            result = head
            head = temp
        
        return result
            
