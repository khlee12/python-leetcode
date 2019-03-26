# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m==n or head is None:
            return head
        # 注意从头节点reverse的情况
        # 链表题最好在头节点之前加一个dummy节点

        dummyNode = ListNode(0)
        dummyNode.next = head
        prev = dummyNode

        # 找到开始reverse之前的节点
        for i in range(m - 1):
            prev = prev.next
        
        # 开始reverse
        result = None
        curr = prev.next
        for i in range(n - m + 1):
            temp = curr.next
            curr.next = result
            result = curr
            curr = temp

        prev.next.next = curr
        prev.next = result

        return dummyNode.next
