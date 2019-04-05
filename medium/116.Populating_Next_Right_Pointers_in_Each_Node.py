# 116. Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # BFS
        if root is None:
            return None
        queue = [root]
        while queue:
            size = len(queue)
            nxt = None
            result = nxt
            for i in range(size):
                ptr = queue.pop(0)
                # print(ptr.val)
                if ptr.right:
                    queue.append(ptr.right)
                if ptr.left:
                    queue.append(ptr.left)
                ptr.next = nxt
                nxt = ptr
        return root
        
