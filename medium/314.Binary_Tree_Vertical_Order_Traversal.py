# 314. Binary Tree Vertical Order Traversal
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q = [(root, 0)]
        result = collections.defaultdict(list)
        while q:
            for node, col in q:
                result[col].append(node.val)
            temp = []
            for node,col in q:
                if node.left:
                    temp.append((node.left, col-1))
                if node.right:
                    temp.append((node.right, col+1))
            q = temp
        
        return [result[key] for key in sorted(result.keys())]
