# 369. Plus One Linked List
# https://leetcode.com/problems/plus-one-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        # declare an array
        val = []
        ptr = head
        # input the value
        while ptr:
            val.append(ptr.val)
            ptr = ptr.next
    
        # do plus one
        flag = 0
        for i in range(len(val)-1, -1, -1):
            if i == len(val)-1:
                val[i],flag = int((val[i]+1)%10),(val[i]+1)//10
                
            else:
                val[i],flag = int((val[i]+flag)%10),(val[i]+flag)//10
                
        # update linked list
        prev = head
        if flag == 1:
            prev = ListNode(1)
            prev.next = head
        
        ptr,i = head, 0
        while ptr:
            ptr.val = val[i]
            ptr = ptr.next
            i+=1
        return prev
