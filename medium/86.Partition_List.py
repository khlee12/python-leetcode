# 86. Partition List
# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # iterate linked list
        small = ListNode(-1)
        small_ptr = small
        big = ListNode(-1)
        big_ptr = big
        
        ptr = head
        while ptr:
            temp = ptr.next
            if ptr.val < x:
                small_ptr.next = ptr
                small_ptr = small_ptr.next
                small_ptr.next = None
                ptr = temp
            else:
                big_ptr.next = ptr
                big_ptr = big_ptr.next
                big_ptr.next = None
            ptr = temp
        
        small_ptr.next = big.next
        
        return small.next
        
