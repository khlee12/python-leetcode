# 285. Inorder Successor in BST
# https://leetcode.com/problems/inorder-successor-in-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        ptr, stacks, flag = root, [], False
        while ptr or stacks:
            while ptr:
                stacks.append(ptr)
                ptr = ptr.left
            ptr = stacks.pop()
            if flag is True:
                return ptr
            if ptr.val == p.val:
                flag = True
            ptr = ptr.right
        return None
