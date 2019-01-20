# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        origin_pointer = head
        new_list = None
        while origin_pointer:
            val = origin_pointer.val
            temp_node = ListNode(val)
            temp_node.next = new_list
            new_list = temp_node
            origin_pointer = origin_pointer.next
        return new_list
