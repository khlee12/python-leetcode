# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        ptr = head
        prev = self
        prev.next = head
        
        i = 0
        while ptr:            
            ptr = ptr.next
            if i > n-1:
                prev = prev.next
            i += 1
        if i == n:
            # remove head
            return head.next
        prev.next = prev.next.next
        return head
