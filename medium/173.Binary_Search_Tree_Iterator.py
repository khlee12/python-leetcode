# 173. Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # 用一个数组来保存中序深度遍历的结果， 再输出下一个节点
        if root is None:
            self.bin_arr = None
        else:
            self.bin_arr = []
            self.pos = 0
            def dfs(node):
                if node is None:
                    return
                dfs(node.left)
                self.bin_arr.append(node.val)
                dfs(node.right)
            dfs(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.bin_arr is None:
            return None
        result = self.bin_arr[self.pos] if self.pos < len(self.bin_arr) else -1
        self.pos += 1
        return result
        
    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return False if self.bin_arr is None or self.pos >= len(self.bin_arr) else True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
