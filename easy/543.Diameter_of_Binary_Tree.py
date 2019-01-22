# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None or not root or (root.left is None and root.right is None):
            return 0
        
        self.result = 0
        # 左子树最长的边+右子树最长的边
        def dfs(node):
            # 终止条件，当到达最终节点时，返回0
            if node == None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 计算左右边的和，如果比当前最大值大，更新当前最大值
            temp_result = left+right
            self.result = max(temp_result, self.result)
            
            # 每次返回的时候需要加1（计算边
            return max(left, right)+1
            
        dfs(root)
        return self.result
            
