# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        values = []
        pointer = head
        while pointer:
            values.append(pointer.val)
            pointer = pointer.next
        while head:
            value = values.pop()
            if head.val != value:
                return False
            head = head.next
        
        return True
