# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        stacks, output = [], []
        curr = root
        # print(curr.val)
        while curr or stacks:
            while curr:
                stacks.append(curr)
                curr = curr.left
            curr = stacks.pop()
            output.append(curr.val)
            curr = curr.right
        return output
