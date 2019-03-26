# 160. Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # get length of two lists
        ptr1,ptr2 = headA,headB
        len1,len2 = 0,0
        while ptr1:
            len1+=1
            ptr1 = ptr1.next
        while ptr2:
            len2 += 1
            ptr2 = ptr2.next
        
        print(len1)
        print(len2)
        
        ptr1,ptr2 = headA,headB
        for i in range(abs(len1-len2)):
            if len1>len2:
                ptr1 = ptr1.next
            else:
                ptr2 = ptr2.next
        
        while ptr1 and ptr2:
            if ptr1 == ptr2:
                return ptr1
            else:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
        return None
