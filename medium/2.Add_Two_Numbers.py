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
        
        l1_pointer = l1
        l2_pointer = l2
        plus_flag = 0
        result = None
        dummy = None
        while l1_pointer or l2_pointer:
            l1_val = l1_pointer.val if l1_pointer else 0
            l2_val = l2_pointer.val if l2_pointer else 0
            temp_sum = l1_val + l2_val + plus_flag
            plus_flag = int(temp_sum/10)
            temp_sum = int(temp_sum%10)
            temp_node = ListNode(temp_sum)

            if result is None:
                result = temp_node
                dummy = result
            else:
                dummy.next = temp_node
                dummy = dummy.next
                
            if l1_pointer:
                l1_pointer = l1_pointer.next
            if l2_pointer:
                l2_pointer = l2_pointer.next
            
        if plus_flag == 1:
            dummy.next = ListNode(1)
        return result
