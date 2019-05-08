# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import *

class Solution:
    def mergeKLists(self, lists):
        dummy = ptr = ListNode(0)
        # insert first node of each list
        heap = []
        for i, l in enumerate(lists):
            if l:
                heappush(heap, (l.val, i))

        while heap:
            val, index = heappop(heap)
            curHead = lists[index]
            ptr.next = curHead
            ptr = ptr.next
            curNext = curHead.next
            curHead.next = None
            curHead = curNext
            if curHead:
                lists[index] = curHead
                heappush(heap, (curHead.val, index))
        
        return dummy.next
