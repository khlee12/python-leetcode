# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        ptr1 = l1
        ptr2 = l2
        
        flag = 0
        dummy = ListNode(-1)
        result = dummy
        
        while ptr1 or ptr2:
            val1 = ptr1.val if ptr1 else 0
            val2 = ptr2.val if ptr2 else 0
            
            val, flag = int((val1+val2+flag)%10), (val1+val2+flag)//10
            node = ListNode(val)
            result.next = node
            result = result.next
            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next
        
        if flag == 1:
            result.next = ListNode(1)
        
        return dummy.next
