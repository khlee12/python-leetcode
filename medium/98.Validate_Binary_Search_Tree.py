# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # InOrder
        # if prev> curr: False
        if not root or root is None:
            return True
        
        stacks = []
        curr = root
        prev = None
        while curr or stacks:
            while curr:
                stacks.append(curr)
                curr = curr.left
            
            curr = stacks.pop()
            if prev is None:
                prev = curr.val
            else:
                if curr.val <= prev:
                    return False
                else:
                    prev = curr.val
            
            curr = curr.right
        
        return True
